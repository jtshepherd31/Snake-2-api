#!/bin/bash

curl "http://localhost:8000/highscores/" \
  --include \
  --request GET \
  --header "Authorization: Bearer ${TOKEN}"

echo
