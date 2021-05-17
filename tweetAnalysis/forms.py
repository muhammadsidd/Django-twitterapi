from django import forms
from .models import Tweeter

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Tweeter
        fields = '__all__'