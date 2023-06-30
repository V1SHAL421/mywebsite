from django import forms
from myapp.models import Post

class WelcomeForm(forms.Form):
    name = forms.CharField(label='Your Name')
    email = forms.EmailField(label='Your Email')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
