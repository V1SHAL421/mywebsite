from django.contrib.auth.models import AbstractUser
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'myapp'


class User(AbstractUser):
    bio = models.TextField()