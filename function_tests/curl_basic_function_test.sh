#!/bin/bash

#authzoed
curl -u email@test.te:aa -i -X GET 127.0.0.1:5000/token

curl -i -X POST -H "Content-Type: application/json" -d '{"email": "email@test.test", "password": "test"}' 127.0.0.1:5000/api/users

curl -u email@test.test:test -i -X GET 127.0.0.1:5000/token
