from django import forms
from .models import Tweeter
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class NewUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username','email','password1','password2', 'first_name', 'last_name']

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Tweeter
        fields = '__all__'