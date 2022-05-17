from dataclasses import field
from django import forms
from django.contrib.auth.models import User




class SignupForm(forms.ModelForm):
    fullname    = forms.CharField(label="", widget  = forms.TextInput(attrs={'class':'form-control input-data','placeholder':'Fullname','autoFocus':'','required':''}))
    email       = forms.CharField(label="", widget  = forms.TextInput(attrs={'class':'form-control input-data','placeholder':'Email','autoFocus':'','required':''}))
    username    = forms.CharField(label="", widget  = forms.TextInput(attrs={'class':'form-control input-data','placeholder':'Matric ID','autoFocus':'','required':''}))
    password    = forms.CharField(label="", widget  = forms.PasswordInput(attrs={'class':'form-control input-data','placeholder':'Password','autoFocus':'','required':''}))
    class Meta:
        model = User
        fields = ['email']


class LoginForm(forms.ModelForm):
    username   = forms.CharField(label="", widget  = forms.TextInput(attrs={'class':'form-control input-data','placeholder':'Matric ID','autoFocus':'','required':''}))
    password    = forms.CharField(label="", widget  = forms.PasswordInput(attrs={'class':'form-control input-data','placeholder':'Password','autoFocus':'','required':''}))
    class Meta:
        model = User
        fields = ['username','password',]

