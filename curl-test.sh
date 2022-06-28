curl --request POST http://localhost:5000/api/timeline_post -d 'name=William&email=williamlin@uchicago.edu&content=Testing my endpoints with postman and curl'

curl --request GET http://localhost:5000/api/timeline_post

curl --request DELETE http://localhost:5000/api/timeline_post
