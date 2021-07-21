curl "http://localhost:8000/highscores/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer ${TOKEN}" \
  --data '{
    "highscore": {
      "id": "'"${ID}"'",
      "email": "'"${EMAIL}"'",
      "score": "'"${SCORE}"'"
    }
  }'

echo
