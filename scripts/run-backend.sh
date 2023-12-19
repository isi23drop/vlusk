#!/bin/bash
#
export DB_URL="postgresql://postgres:admin@localhost:5432/db"
export FLASK_APP="app.py"
source ../venv/bin/activate
cd ./backend/app/ || exit
#flask --app app run --debug
flask --debug run
