# How to build docker image

docker build -t frontend-dev .

docker run -p 8080:80 nginx-frontend:latest


# build script
docker build -t frontend-dev:latest .