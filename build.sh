image_name=$(cat image_name.txt)
docker build . -t "$image_name"
