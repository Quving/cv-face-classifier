#!/bin/bash

if [[ "$UPDATE_WEIGHTS" -eq "1" ]]; then
    echo "Download Model from nextcloud."
    rm -rf cnn/class_indices cnn/models
    wget -O class_indices.zip http://nextcloud.quving.com/s/GkdP5QoaPJpEs2d/download && \
        unzip class_indices.zip -d cnn
    wget -O models.zip http://nextcloud.quving.com/s/ktXiwxgiAgxrA2L/download && \
        unzip models.zip -d cnn
    rm -f class_indices.zip models.zip
fi

python2.7 letsfaceit.py
