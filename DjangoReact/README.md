## Project Setup
    -   python3 -m pip install pipenv --upgrade
    -   pipenv install --python 3.6 django

## Activate environment
    -   pipenv shell

## Django project & run server
    -   django-admin startproject DjangoReact .
    -   python manage.py runserver

## Django application
    -   ./manage.py startapp books

## Books model
    ```
    from django.db import models
    class Books(models.Model):
        name = models.TextField(blank=False, null=False)
        author = models.TextField(blank=False, null=False)
        description = models.TextField(blank=True, null=True)
        image = models.FileField(upload_to='images/', blank=True, null=True)
    ```
## Migrate
    -   python manage.py makemigrations
    -   python manage.py migrate

## Save data from shell
    -   pipenv shell
        -   from books.models import Books
        -   obj = Books()
        -   obj.name = 'Book 1'
        -   obj.author = 'Book 1 author'
        -   obj.description = 'Its first book by an author'
        -   obj.save()
        -   fb = Books.objects.get(id=1)
        -   fb.name
        -   exit()
