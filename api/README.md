# API Methods
GET - The GET method requests a representation of the specified resource. Requests using GET should only retrieve data. < br />
HEAD - The HEAD method asks for a response identical to a GET request, but without the response body. < br />
POST - The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server.
PUT - The PUT method replaces all current representations of the target resource with the request content.
DELETE - The DELETE method deletes the specified resource.
CONNECT - The CONNECT method establishes a tunnel to the server identified by the target resource.
OPTIONS - The OPTIONS method describes the communication options for the target resource.
TRACE -The TRACE method performs a message loop-back test along the path to the target resource.
PATCH -The PATCH method applies partial modifications to a resource.

Publish an API - Ref: https://www.docker.com/blog/getting-started-with-docker-using-node-jspart-i/

# Docker run
docker run -p 8080:8000 node-docker:latest

# POST
curl --request POST \
  --url http://127.0.0.1:8080/test \
  --header 'content-type: application/json' \
  --data '{
	"msg": "testing"
}'

# DELETE
curl -X "DELETE" http://localhost:8080/test/<ID> 

fyi - <ID> was assigned randomnly since the original POST did not have an ID

# GET
curl http://127.0.0.1:8000/test

# Dockerfile
docker build --tag node-docker . --latest
