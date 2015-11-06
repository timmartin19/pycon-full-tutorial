#!/usr/bin/env bash


#Hello world examples
curl http://localhost:5000/hello/ | jq .

curl http://localhost:5000/hello/Bob/ | jq .

curl http://localhost:5000/hello/Bob/ -H "Accept:application/hal+json" | jq .

# Relationship examples
curl http://localhost:5000/hello/?name=Bob | jq .

curl http://localhost:5000/related/Bob/ | jq .

# Full example
# Get All Posts
curl http://localhost:5000/api/post/ | jq .

# Create Post
curl -H "Content-Type: application/json" -X POST -d '{"username":"xyz","post_text":"xyz"}' http://localhost:5000/api/post/ | jq .

# Get Individual
curl http://localhost:5000/api/post/1/ | jq .

# Update Post
curl -H "Content-Type: application/json" -X PATCH -d '{"username": "bob"}' http://localhost:5000/api/post/1/ | jq .

# Create Comment
curl -H "Content-Type: application/json" -X POST -d '{"username": "sally", "comment_text": "Awesome", "post_id": 1}' http://localhost:5000/api/comment/ | jq .

curl -H "Content-Type: application/json" -X POST -d '{"username":"Bob","comment_text":"This is my comment"}' http://localhost:5000/api/post/1/create_comment/ | jq .
