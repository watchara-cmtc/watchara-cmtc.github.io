from django.db import models

# Create your models here.


class testdata(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
