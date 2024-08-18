# How to build docker image

docker build -t nginx-frontend .

docker rund -p 8080:80 nginx-frontend:latest
