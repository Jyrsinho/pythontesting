image_name=$(cat image_name.txt)
docker rm -f "$image_name"
