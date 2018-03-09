#!/bin/bash
set -e
ssh tams225 'bash -c "bash automation/update_model.sh"'
echo "Update model locally."

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

echo "Job finished."
