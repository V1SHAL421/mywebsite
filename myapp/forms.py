from django import forms
from myapp.models import Post
from .models import User
from django.core.validators import RegexValidator
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

class SignUpForm(forms.ModelForm):
    class Meta: # provides metadata about sign up form
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'bio']
        widgets = { 'bio': forms.Textarea() }
        
    new_password = forms.CharField( # states regulations for password
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
    password_confirmation = forms.CharField(label='Confirm Password', widget=forms.PasswordInput()) # confirms password

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password'].widget = forms.PasswordInput()
        self.fields['password_confirmation'].widget = forms.PasswordInput()

        # Create a crispy form helper and define the form layout
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Sign up'))
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'username',
            'email',
            'bio',
            'new_password',
            'password_confirmation',
        )

    def clean(self): # overidden to perform additional validation and error handling
        super().clean() # creates instance var for class
        new_password = self.cleaned_data.get('new_password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if new_password != password_confirmation:
            self.add_error('password_confirmation', 'Confirmation does not match password.')
        # checks to see if passwords match

    def save(self): # overidden to save new User object to database
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

class LogInForm(forms.Form): # user login functionality
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class PostForm(forms.ModelForm): # creating posts
    class Meta:
        model = Post
        fields = ['date', 'title', 'content']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': True}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Create'))
        self.helper.layout = Layout(
            Field('date', css_class='form-control', required=True),
            Field('title', css_class='form-control', required=True),
            Field('content', css_class='form-control', required=True),
        )
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'required': 'required'})
