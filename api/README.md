Publish an API

npm init -y
npm install ronin-server ronin-mocks
touch server.js

Ref: https://www.docker.com/blog/getting-started-with-docker-using-node-jspart-i/

# POST
curl --request POST \
  --url http://localhost:8000/test \
  --header 'content-type: application/json' \
  --data '{
	"msg": "testing"
}'

# GET
curl http://localhost:8000/test


# Dockerfile
docker build --tag node-docker . --latest
