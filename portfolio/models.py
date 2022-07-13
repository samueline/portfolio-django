import email
from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField
# from django.forms import EmailField
# Create your models here.


class Project(models.Model):
    title = CharField(max_length=100)
    descripcion = CharField(max_length=250)
    image = ImageField(upload_to='portfolio/images/')
    url = URLField(blank=True)

class Contact(models.Model):
    user = CharField(max_length=100)
    email = CharField(max_length=100)
    descripcion = CharField(max_length=100)
