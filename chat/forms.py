from django import forms
#from django.core.excepions import ObjectDoesNotExist
import re
class RegistrationForm(forms.Form):
    username=forms.CharField(label="Username",max_length=30)
    email=forms.EmailField(label='Email')
    password=forms.CharField(label='Password', widget=forms.PasswordInput())
    cpassword=forms.CharField(label='Confirm Password', widget=forms.PasswordInput())
class LoginForm(forms.Form):
    username=forms.CharField(label="username",max_length=30)
    email=forms.EmailField(label="email")
    password=forms.CharField(label="password",widget=forms.PasswordInput())
