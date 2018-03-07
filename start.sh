#!/bin/bash

if [[ "$UPDATE_WEIGHTS" -eq "1" ]]; then
    echo "Download Model from nextcloud."
    rm -rf cnn/class_indices cnn/models
    wget -O class_indices.zip $NC_CLASS_INDICES_URL && \
        unzip class_indices.zip -d cnn
    wget -O models.zip $NC_MODEL_URL && \
        unzip models.zip -d cnn
    rm -f class_indices.zip models.zip
fi

python2.7 letsfaceit.py
