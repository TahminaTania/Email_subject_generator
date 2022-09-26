from dataclasses import fields
from django.core import validators
from django import forms
from django.forms import ModelForm
# from .models import profiles, subscriber
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class inputForm(forms.ModelForm):
#     class Meta:
#         model = inputs
#         # fields = ["word"]
#         cetagory = forms.ChoiceField(
#             choices=[(x, x) for x in ['Benefit', 'Pin-point', 'Necessity']])
#         word = forms.CharField()

#         widgets = {
#             'cetagory': forms.TextInput(attrs={'class': 'form-control'}),
#             'word': forms.EmailInput(attrs={'class': 'form-control'}),
#         }
