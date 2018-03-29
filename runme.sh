#!/usr/bin/env bash
sh rm_migrations.sh
rm db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate