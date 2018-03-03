#!/bin/bash

source ./venv/bin/activate
export APP_RUNNING_ENV=DEV
export FLASK_APP=shop
export FLASK_DEBUG=1
flask run
