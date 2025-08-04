#!/bin/bash

RANDOM_ID=$(date +%s)
NAME="Test User $RANDOM_ID"
EMAIL="test$RANDOM_ID@example.com"
CONTENT="Test post $RANDOM_ID"

echo "Testing timeline POST endpoint..."
echo "Posting data: name=$NAME, email=$EMAIL, content=$CONTENT"
echo "Response:"
curl -s -X POST -d "name=$NAME" -d "email=$EMAIL" -d "content=$CONTENT" http://localhost:5000/api/timeline_post
echo ""
echo ""

echo "Testing timeline GET endpoint..."
echo "Response:"
curl -s -X GET http://localhost:5000/api/timeline_post
echo ""
echo ""

echo "Checking if our test post exists..."
echo "Searching for: $NAME"
RESULT=$(curl -s -X GET http://localhost:5000/api/timeline_post | grep "$NAME")
if [ -n "$RESULT" ]; then
    echo "✅ Test post found!"
    echo "Match: $RESULT"
else
    echo "❌ Test post not found"
fi
