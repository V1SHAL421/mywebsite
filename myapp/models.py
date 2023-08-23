from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

class Post(models.Model):
    date = models.DateField()
    title = models.TextField(max_length=50, default='I had fun today!')
    content = models.TextField()
    

    class Meta:
        app_label = 'myapp'


class User(AbstractUser):
    username = models.CharField(
        max_length=30, 
        unique=True,
        validators=[RegexValidator(
            regex=r'^@\w{3,}$',
            message='Username must consist of @ followed by at least three alphanumericals'
        )]
        )
    first_name = models.CharField(
        max_length=30,
        blank=False
    )

    last_name = models.CharField(
        max_length=30,
        blank=False
    )

    email = models.EmailField(
        unique=True,
        blank=False,

    )
    
    bio = models.CharField(
        max_length=400,
        blank=True
        ) # AbstractUser class variables + bio
    # first_name = models.CharField(label='Your Name', max_length=30)
    # surname = models.CharField(label='Your Surname', max_length=30)
    # bio = models.CharField(label='Bio', max_length=500)
    # email = models.EmailField(label='Your Email')
    # new_password = models.CharField(label='Password', widget=models.PasswordInput())
    # password_confirmation = models.CharField(label='Confirm Password', widget=models.PasswordInput())
