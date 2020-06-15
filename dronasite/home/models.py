from django.db import models

# Create your models here.

class streams(models.Model):
    id : models.IntegerField()
    title : models.CharField(max_length=25)
    img : models.CharField(max_length=150)