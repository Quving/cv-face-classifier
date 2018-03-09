#!/bin/bash

ssh tams225 'bash -c "bash automation/update_model.sh"'

wget $NC_URL/index.php/s/$NC_MODEL_TOKEN/download && \
    unzip download -d cnn && \
    rm download

wget $NC_URL/index.php/s/$NC_TRAINING_TOKEN/download && \
    unzip download  -d cnn && \
    rm download

wget $NC_URL/index.php/s/$NC_CLASS_INDICES_TOKEN/download && \
    unzip download -d cnn && \
    rm download
