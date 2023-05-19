from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from catalog.models import medicine

class signform(UserCreationForm):
    class meta:
        model=User
        field=['username','email','password1','password2']



class medicineForms(forms.ModelForm):
    class Meta:
        model = medicine
        fields ='__all__'
