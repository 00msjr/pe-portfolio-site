#!/bin/bash

RANDOM_ID=$(date +%s)
NAME="Test User $RANDOM_ID"
EMAIL="test$RANDOM_ID@example.com"
CONTENT="Test post $RANDOM_ID"

curl -s -X POST -d "name=$NAME" -d "email=$EMAIL" -d "content=$CONTENT" http://localhost:5000/api/timeline_post

curl -s -X GET http://localhost:5000/api/timeline_post | grep "$NAME"
