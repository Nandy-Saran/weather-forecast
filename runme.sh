#!/usr/bin/env bash
sh rm_migrations.sh
rm db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate
./manage.py loaddata backup/crops.json
./manage.py loaddata backup/disease.json
./manage.py loaddata backup/place.json
./manage.py loaddata backup/satweather.json