
curl "http://localhost:8000/highscore/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "highscore": {
      "email": "'"${EMAIL}"'",
      "score": "'"${SCORE}"'"
    }
  }'

echo
