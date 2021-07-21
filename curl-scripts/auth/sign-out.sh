curl "http://localhost:8000/sign-out/" \
  --include \
  --request DELETE \
  --header "X-CSRFToken: ${CSRF}" \
  --header "Authorization: Bearer ${TOKEN}" \

echo
