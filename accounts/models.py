from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
