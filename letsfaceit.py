#!/usr/bin/python

import os
import cv2
import h5py
import math
import time
import json
import pickle
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from flask import Flask, request, Response, jsonify
from flask_restful import Resource, Api

from keras import optimizers
from keras import applications
from keras.models import Sequential
from keras.models import model_from_json
from keras.layers import Dropout, Flatten, Dense
from keras.utils.np_utils import to_categorical
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img, array_to_img

model_bottleneck = None
model_classifier = None
class_dictionary = None
label_dictionary = None
app = Flask(__name__)
top_model_path = 'cnn/models/top_model_2_classes'
class_indices_path = 'cnn/class_indices/class_indices_2_classes.npy'

# Initialize variables used for prediction.
def initialize():
    global model_bottleneck
    global model_classifier
    global model_bottleneck
    global class_dictionary
    model_bottleneck = getModelBottleneck()
    model_classifier = getModelClassifier()
    class_dictionary = np.load(class_indices_path).item()

# Return model ready to classify images.
def getModelClassifier():
    model = load_model(top_model_path)
    model._make_predict_function()

    global graph
    graph = tf.get_default_graph()
    return model

# Return model ready to extract features from images.
def getModelBottleneck():
    model = applications.VGG16(include_top=False, weights='imagenet')
    model._make_predict_function()

    global graph
    graph = tf.get_default_graph()
    return model

# Return a label to given image.
def predict_image(np_image):
    global model_bottleneck
    global model_classifier
    global class_dictionary
    global graph
    with graph.as_default():
        bottleneck_prediction = model_bottleneck.predict(np_image)

        # classification
        class_predicted = model_classifier.predict_classes(bottleneck_prediction)
        class_predicted_proba = model_classifier.predict_proba(bottleneck_prediction)

        inID = class_predicted[0]
        inv_map = {v: k for k, v in class_dictionary.items()}
        label = inv_map[inID]
        print("Image ID: {}, Label: {}".format(inID, label))

        return {"classname": label, "probability": class_predicted_proba}

# Load model structure and its weights.
def load_model(filename):
    with open(filename + '.json', 'r') as file:
        model = model_from_json(file.read())
        file.close()

    model.load_weights(filename + '.h5')
    return model

@app.route('/api/predict', methods=['POST'])
def get_label():
    post= request.json
    if post is None:
        return jsonify({"error": "Where is the request data?"})

    for key in ["image", "mode"]:
        if not key in post.keys():
            return jsonify({"error": "I think you've missed the key '" + key + "'"})
    image_np = np.array(json.loads(post["image"]))
    print len(image_np)
    cv2.imwrite("tmp.jpg", image_np)
    np_image = load_img("tmp.jpg", target_size=(224, 224))
    np_image = img_to_array(np_image)
    np_image = np_image / 255.0
    np_image = np.expand_dims(np_image, axis=0)
    actual_prediction = predict_image(np_image)
    print actual_prediction

    return jsonify({"label": actual_prediction["classname"], "probability": str(actual_prediction["probability"])})

if __name__ == '__main__':
    initialize()
    api = Api(app)
    app.run(host='0.0.0.0', port=6500)
