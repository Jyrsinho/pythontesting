port=${1:-9000}

image_name=$(cat image_name.txt)
docker run -p "$port":8000 --name "$image_name" --restart unless-stopped -d "$image_name"

