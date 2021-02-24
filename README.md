# Start study_framework

### gunicorn
gunicorn main:application

### uwsgi
// не забывать про название переменной/класса/функции, т.к.: It is called “application” as this is the default function that the uWSGI Python loader will search for (but you can obviously customize it) - [link](https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html#the-first-wsgi-application)


uwsgi --http :8000 --wsgi-file main.py
