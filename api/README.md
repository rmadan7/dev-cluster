# Submit curl requests to the API endpoints

<!-- curl -X POST -H “Authorization: Bearer INSERT_TOKEN_HERE” \
-H “Content-Type: application/json” \
-H “Accepts: application/json” “http://www.exampleapi.com" -->

curl -H "Content-Type: application/json" -X POST http://localhost:50100/sum{x:3,y:5}

-H “Content-Type: application/json” \
-H “Accepts: application/json” “http://www.exampleapi.com"