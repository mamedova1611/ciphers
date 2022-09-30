from django.db import models

class CipherModel(models.Model):
    key = models.CharField(max_length=1000)
    text= models.CharField(max_length=1000)
