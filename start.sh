#!/bin/bash

if [[ "$UPDATE_WEIGHTS" -eq "1" ]]; then
    # Variables
    NC_MODEL_TOKEN='cXAcZ26mPDfjzMe'
    NC_TRAINING_TOKEN="PGLw5AP8sdiesYW"
    NC_CLASS_INDICES_TOKEN='iL3xgnYGyCrw9zM'
    NC_URL='http://nextcloud.quving.com'

    rm -rf cnn/models cnn/training cnn/class_indices cnn/bottleneck_features

    wget $NC_URL/index.php/s/$NC_MODEL_TOKEN/download && \
        unzip download -d cnn && \
        rm download

    wget $NC_URL/index.php/s/$NC_TRAINING_TOKEN/download && \
        unzip download  -d cnn && \
        rm download

    wget $NC_URL/index.php/s/$NC_CLASS_INDICES_TOKEN/download && \
        unzip download -d cnn && \
        rm download
fi

python2.7 letsfaceit.py
