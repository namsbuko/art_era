from django.db import models
from profile.models import Profile


class Painting(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,
                              related_name='paintings')

    image = models.FileField(upload_to='painting/%Y/%m/%d')
    cost = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    creation_year = models.PositiveSmallIntegerField()
    location = models.CharField(max_length=100)
    height = models.PositiveSmallIntegerField()
    width = models.PositiveSmallIntegerField()
    material = models.CharField(max_length=100)
    technique = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    genre = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
