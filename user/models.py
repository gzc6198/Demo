from django.db import models


# Create your models here.
class User(models.Model):
    # SEX = (
    #     ('M', 'man'),
    #     ('W', 'woman'),
    #     ('BM', 'baomi')
    # )
    nickname = models.CharField(max_length=64)
    password = models.CharField(max_length=256)
    age = models.IntegerField()
    icon = models.ImageField()
    # sex = models.CharField(max_length=8,choices=SEX)
    sex = models.CharField(max_length=8)