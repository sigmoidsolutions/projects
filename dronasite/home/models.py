from django.db import models

# Create your models here.

class streams(models.Model):

    title = models.CharField(max_length=25)
    img = models.ImageField(upload_to='pictures')