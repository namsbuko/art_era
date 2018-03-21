from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fio = models.CharField(max_length=100, blank=True, default='')
    phone = models.CharField(max_length=15, blank=True, default='')

    city = models.CharField(max_length=30, blank=True, default='')
    longitude = models.FloatField(blank=True, default=0.0)
    latitude = models.FloatField(blank=True, default=0.0)
    birthday = models.CharField(max_length=30, blank=True, default='')
    about_yourself = models.TextField(max_length=5000, blank=True, default='')
    status = models.CharField(max_length=150, blank=True, default='')
    avatar = models.FileField(upload_to='avatars/%Y/%m/%d', blank=True, null=True)

    @property
    def email(self):
        return self.user.email

    @property
    def gallery_cost(self):
        total = self.paintings.aggregate(total=Sum('cost')).get('total')
        return total if total else 0

    @property
    def paintings_count(self):
        return self.paintings.count()

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
