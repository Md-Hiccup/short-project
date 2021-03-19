# Flask Todo App
[Reference](https://youtu.be/Z1RJmh_OqeA)

## Install Flask & SQLAlchemy
>   $ pip install flask flask-sqlalchemy

## Create Sqlite DB
```
$ python
>>> from app import db
>>> db.create_all()
```

## Heroku Installation
```
$ sudo snap install --classic heroku
$ heroku login
$ pip install gunicorn
```

## Requirements
>   $ pip freeze > requirements.txt

## Push code in Heroku
```
$ git init
$ git add .
$ git commit -m 'init app'
$ heroku create flaskTodoApp
$ git remote -v
$ git push heroku master
```

## To run app on Heroku server
```
$ touch Procfile
web: gunicorn app:app
```
