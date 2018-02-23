#!/bin/bash

curl -i -X POST -H "Content-Type: application/json" -d '{"email": "email@test.test", "password": "test"}' 127.0.0.1:5000/api/users
