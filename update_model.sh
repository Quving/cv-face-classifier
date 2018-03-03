set -e
nc_path="$HOME"/Nextcloud/github/cv-face-classifier/
rsync -r -v tams223:/homeL/project2017/2ngu/cv-face-classifier/cnn/models "$nc_path"
rsync -r -v tams223:/homeL/project2017/2ngu/cv-face-classifier/cnn/class_indices "$nc_path"

cd $nc_path && zip -r models.zip models
cd $nc_path && zip -r class_indices.zip class_indices
