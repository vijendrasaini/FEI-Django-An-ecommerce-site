# from django import forms
# from .models import User

# class UserForm(forms.Form):
#     name = forms.CharField(label="Enter Name", initial="vijendra")
#     email = forms.CharField(label="Enter Email", initial="vijendra@gmail.com")
#     password = forms.CharField(widget=forms.PasswordInput, label="Enter Your password")

# class UserModelForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['name', 'password', 'email']

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCustomForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username']
        labels = {'email' : 'Enter Email'}