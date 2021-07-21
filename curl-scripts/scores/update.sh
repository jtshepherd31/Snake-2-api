#!/bin/bash

curl "http://localhost:8000/highscores/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer ${TOKEN}" \
  --data '{
    "highscore": {
      "email": "'"${EMAIL}"'",
      "score": "'"${SCORE}"'"
    }
  }'

echo
