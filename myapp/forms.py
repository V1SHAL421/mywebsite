from django import forms
from myapp.models import Post
from .models import User

# class SignUpForm(forms.ModelForm):
#     first_name = forms.CharField(label='Your Name', max_length=30)
#     surname = forms.CharField(label='Your Surname', max_length=30)
#     username = forms.CharField(label='Username', max_length=30)
#     bio = forms.CharField(label='Bio', max_length=500)
#     email = forms.EmailField(label='Your Email')
#     new_password = forms.CharField(label='Password', widget=forms.PasswordInput())
#     password_confirmation = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())
class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'bio']
        widgets = { 'bio': forms.Textarea() }
        
    new_password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password_confirmation = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
