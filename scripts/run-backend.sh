#!/bin/bash
#
#

export DB_URL="postgresql://admin:Passw0rd@localhost:5432/"
export FLASK_APP="app.py"
source ../venv/bin/activate
cd ./backend/app/ || exit
#flask --app app run --debug
flask --debug run
