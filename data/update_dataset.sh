filename="original_samples"
if [ -d "$filename" ]; then rm -rf "$filename"; fi
wget -O $filename.zip http://nextcloud.quving.com/s/rMkz8rbCAYmfZT4/download
unzip $filename.zip
rm $filename.zip


