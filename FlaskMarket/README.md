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

### Drop & Recreate db
``` 
$ python
>>> from market.models import db
>>> db.drop_all()       ## It will delete all the data from db
>>> db.create_all()
```

### Created dummy data in db
```
## Creating User
>>> from market.models import User, Item
>>> u1 = User(username='abc', email_address='abc@abc.com', password_hash='123456')
>>> db.session.add(u1)
>>> db.session.comit()
>>> User.query.all()

## Creating items
>>> item1 = Item(name='iphone', price=500, barcode='819283746512', description='desc')
>>> db.session.add(item1)
>>> db.session.commit()
>>> item1 = Item(name='laptop', price=1000, barcode='5422283746512', description='desc 2')
>>> db.session.add(item1)
>>> db.session.commit()
>>> Item.query.all()

## Assigning Item with owner
>>> i1 = Item.query.filter_by(name='iphone')
>>> i1
<flask_sqlalchemy.BaseQuery object at 0x10935f2b0>
>>> i1 = Item.query.filter_by(name='iphone').first()
>>> i1
Item iphone
>>> i1.owner = User.query.filter_by(username='abc').first().id
>>> db.session.add(i1)
>>> db.session.commit()

## In case if needed to rollback
>>> db.session.rollback()

## Verify item owner
>>> i = Item.query.filter_by(name='iphone').first()
>>> i.owned_user    ## Use backref value
<User 1>
```