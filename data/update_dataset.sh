filename="original_samples"
if [ -d "$filename" ]; then rm -rf "$filename"; fi
wget -O $filename.zip $NC_DATASET_URL
unzip $filename.zip
rm $filename.zip


