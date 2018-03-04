from django.db import models

from painting.models import Painting


class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True)

    paintings = models.ManyToManyField(Painting, related_name='collections')
