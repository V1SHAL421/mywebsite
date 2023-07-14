from django.contrib.auth.models import AbstractUser
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'myapp'


class User(AbstractUser):
    bio = models.TextField() # AbstractUser class variables + bio

#    first_name = forms.CharField(label='Your Name', max_length=30)
#     surname = forms.CharField(label='Your Surname', max_length=30)
#     username = forms.CharField(label='Username', max_length=30)
#     bio = forms.CharField(label='Bio', max_length=500)
#     email = forms.EmailField(label='Your Email')
#     new_password = forms.CharField(label='Password', widget=forms.PasswordInput())
#     password_confirmation = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())