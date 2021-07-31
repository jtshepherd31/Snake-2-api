#!/bin/bash

curl "http://localhost:8000/highscores/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Bearer ${TOKEN}"
  --data '{
    "highscore": {
      "owner": "'"${OWNER}"'",
    }
  }'

echo
