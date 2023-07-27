from django import forms
from myapp.models import Post
from .models import User
from django.core.validators import RegexValidator

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'bio']
        widgets = { 'bio': forms.Textarea() }
        
    new_password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        validators=[
            RegexValidator(
                regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)',
                message='Password must contain an uppercase character, a lowercase' 
                        'character, and a number.'
            )
        ]
    )
    password_confirmation = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())

    def clean(self):
        super().clean() # creates instance var for class
        new_password = self.cleaned_data.get('new_password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if new_password != password_confirmation:
            self.add_error('password_confirmation', 'Confirmation does not match password.')

    def save(self):
        super().save(commit=False)
        user = User.objects.create_user(
                self.cleaned_data.get('username'),
                first_name = self.cleaned_data.get('first_name'),
                last_name = self.cleaned_data.get('last_name'),
                email = self.cleaned_data.get('email'),
                bio = self.cleaned_data.get('bio'),
                password = self.cleaned_data.get('new_password'),
                
            )
        return user

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
