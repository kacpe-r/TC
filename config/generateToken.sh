#!/bin/bash
# sh ./config/generateToken.sh existingLogin existingPassword tokenName

OUTPUT_FILE="token"
if [ -f "./config/$OUTPUT_FILE" ]; then
    rm ./config/$OUTPUT_FILE
fi

if ! [ $3 ]; then
    echo "Not all parameters provided. Try:"
    echo "sh ./config/generateToken.sh login password tokenName"
    exit 1
fi

login=$1
password=$2
token_name=$3
curl -X 'POST' \
  'http://localhost:8111/app/rest/users/'$login'/tokens' \
  -H 'accept: application/xml' \
  -H 'Content-Type: application/json' \
  -u "$login":"$password"\
  -d '{
    "name": "'"$token_name"'"
}' | grep -oP '(?<=value\=\").*(?=[\"])' >> ./config/$OUTPUT_FILE
