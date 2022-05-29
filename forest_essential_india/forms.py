

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCustomForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username']
        labels = {'email' : 'Enter Email'}