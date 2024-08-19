# How to build docker image

docker build -t nginx-frontend .

docker run -p 8080:80 nginx-frontend:latest
