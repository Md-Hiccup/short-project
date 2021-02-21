from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.TextField(blank=False, null=False)
    author = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
