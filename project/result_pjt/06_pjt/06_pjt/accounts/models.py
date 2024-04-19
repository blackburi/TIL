from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    nickname = models.CharField(max_length=30, blank=True)
    followings = models.ManyToManyField(settings.AUTH_USER_MODEL, symmetrical=False, related_name = 'followers')  