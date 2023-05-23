from django import forms
from grocery.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class contactform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=contact1

class reviewform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=review

class subscribeform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=newsletter

class faqform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=faq

class signupform(UserCreationForm):
    first_name=forms.CharField(
        widget=forms.TextInput(
        attrs={
        "class":"form-control",
        'placeholder':'First Name'}))

    last_name=forms.CharField(
        widget=forms.TextInput(
        attrs={
        "class":"form-control",
        'placeholder':'Last Name'}))
    
    username=forms.CharField(
        widget=forms.TextInput(
        attrs={
        "class":"form-control",
        'placeholder':'Username'}))
    
    email=forms.CharField(
        widget=forms.TextInput(
        attrs={
        "class":"form-control",
        'placeholder':'Email'}))
    
    password1=forms.CharField(
        widget=forms.PasswordInput(
        attrs={
        "class":"form-control",
        'placeholder':'Password'}))
    
    password2=forms.CharField(
        widget=forms.PasswordInput(
        attrs={
        "class":"form-control",
        'placeholder':'Confirm Password'}))
    
    class Meta:
        fields=('first_name','last_name','username','email','password1','password2')
        model=User  

class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password1=forms.CharField(max_length=50, widget=forms.PasswordInput)
