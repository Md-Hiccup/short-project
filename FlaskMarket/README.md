## Project on Flask

## Install Flask
```
$ mkdir FlaskMarket
$ cd FlaskMarket
$ pipenv shell
$ pip install flask
```

## setting flask
```
$ export FLASK_APP=market.py
```

## Setting Debug mode on - helps to restart server on any changes
```
$ export FLASK_DEBUG=1
```

## run flask server
```
$ flask run
```

## Install SQLAlchemy
```
$ pip install flask-sqlalchemy
```

## Create Sqlite DB
```
$ python
>>> from app import db
>>> db.create_all()
```