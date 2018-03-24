cd into project folder and do all  this cmd
```bash
pip install -r requirements.txt
sh rm_migrations.sh
rm db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate
```
```
python3 manage.py shell
```

In the django shell type the following
```djangotemplate
execfile('setup.py')
```
Open in new terminal and cd into project folder
```djangotemplate
./manage.py loaddata disease.json
```

Finally run the server by this command

```bash
python3 manage.py runserver
```
