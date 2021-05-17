## Project on Flask

### Install Flask
```
$ mkdir FlaskMarket
$ cd FlaskMarket
$ pipenv shell
$ pip install flask
$ flask --version
```

### setting flask
```
$ export FLASK_APP=market.py
```

### Setting Debug mode on - helps to restart server on any changes
```
$ export FLASK_DEBUG=1
```

### run flask server
```
$ flask run
```

### Install SQLAlchemy, it allows to write database table with python classes
```
$ pip install flask-sqlalchemy
```

### Create Sqlite DB and insert data
```
$ python
>>> from market import db
>>> db.create_all()
>>> from model import Item
>>> item1 = Item(name='iphone', price=500, barcode='819283746512', description='desc')
>>> db.session.add(item1)
>>> db.session.commit()
>>> Item.query.all()
[<Item 1>]
>>> Item.query.filter_by(price=500)
<flask_sqlalchemy.BaseQuery object at 0x000000...>
```

