#!/bin/bash

curl "http://localhost:8000/highscores/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
