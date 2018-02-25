#!/usr/bin/env python
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

top_model_path = 'models/top_model_2_classes'
class_indices_path = 'class_indices/class_indices_2_classes.npy'

# Return model ready to classify images.
def getModelClassifier():
    model = load_model(top_model_path)
    model._make_predict_function()

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

        inID = class_predicted[0]
        inv_map = {v: k for k, v in class_dictionary.items()}
        label = inv_map[inID]
        return label

# Initialize variables used for prediction.
def initialize():
    global model_bottleneck
    global model_classifier
    global model_bottleneck
    global class_dictionary
    model_bottleneck = getModelBottleneck()
    model_classifier = getModelClassifier()
    class_dictionary = np.load(class_indices_path).item()

# Load model structure and its weights.
def load_model(filename):
    print "Load model from", filename
    with open(filename + '.json', 'r') as file:
        model = model_from_json(file.read())
        file.close()

    model.load_weights(filename + '.h5')
    return model


def test(directory, expected_prediction):
    absolute_path_to_source = os.getcwd() + '/' + directory

    # Collect a list of names of the source directory.
    files = [f for f in os.listdir(absolute_path_to_source) if ".jpg" in f]
    print len(files), "images found in", directory

    # Statistics
    no_of_samples = len(files)
    correct_predictions = 0.0

    for index in range(len(files)) :
        relative_image_path = directory + '/' + files[index]

        orig = cv2.imread(relative_image_path)

        np_image = load_img(relative_image_path, target_size=(224, 224))
        np_image = img_to_array(np_image)
        np_image = np_image / 255.0
        np_image = np.expand_dims(np_image, axis=0)

        actual_prediction = predict_image(np_image)

        if actual_prediction == expected_prediction:
            correct_predictions += 1

    return correct_predictions/len(files)*100

def test_predictions():
    print "Accuracy",test("../data/test/chris", "chris")
    print "Accuracy",test("../data/test/vinh", "vinh")

if __name__ == '__main__':
    initialize()
    test_predictions()

