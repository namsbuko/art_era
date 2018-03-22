from django.db import models
from profile.models import Profile


class Painting(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,
                              related_name='paintings')

    image = models.FileField(upload_to='painting/%Y/%m/%d')
    cost = models.PositiveIntegerField(default=10000)
    name = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=100, default='', blank=True)
    creation_year = models.PositiveSmallIntegerField(default=2000)
    location = models.CharField(max_length=100, default='', blank=True)
    height = models.PositiveSmallIntegerField(default=100)
    width = models.PositiveSmallIntegerField(default=100)
    material = models.CharField(max_length=100, default='холст')
    description = models.TextField(max_length=1000, default='', blank=True)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)

    TECHNIQUE_CHOICES = (
        ('Масло', 'Масло'),
        ('Гуашь', 'Гуашь'),
        ('Пастель', 'Пастель'),
        ('Тушь', 'Тушь'),
        ('Акварель', 'Акварель'),
    )
    TECHNIQUES = ('Масло', 'Гуашь', 'Пастель', 'Тушь', 'Акварель')
    technique = models.CharField(max_length=100, choices=TECHNIQUE_CHOICES)

    GENRE_CHOICES = (
        ('Абстракционизм', 'Абстракционизм'),
        ('Гиперреализм', 'Гиперреализм'),
        ('Городской пейзаж', 'Городской пейзаж'),
        ('Импрессионизм', 'Импрессионизм'),
        ('Классицизм', 'Классицизм'),
        ('Морской пейзаж', 'Морской пейзаж'),
        ('Натюрморт', 'Натюрморт'),
        ('Пейзаж', 'Пейзаж'),
        ('Портрет', 'Портрет'),
        ('Сюрреализм', 'Сюрреализм'),
    )
    GENRES = ('Абстракционизм', 'Гиперреализм', 'Городской пейзаж', 'Импрессионизм',
              'Классицизм', 'Морской пейзаж', 'Натюрморт', 'Пейзаж',
              'Портрет', 'Сюрреализм')
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)

    def __str__(self):
        return self.name

