#!/bin/bash
#
export DB_URL="postgresql://postgres:admin@localhost:5432/db"
source ../venv/bin/activate
cd ./backend/ || exit
flask --app app run --debug
