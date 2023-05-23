from django import forms
from dashboard.models import *
from django.contrib.auth.forms import PasswordChangeForm


class addproform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Product

class addcatform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Category

class Productform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Product

class Categoryform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Category

class addsuppform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Supplier

class Supplierform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Supplier 

class Purchaseform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Purchase         

class addpurform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Purchase

class PasswordChangeForm(PasswordChangeForm):
    oldpassword=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Enter Old Password"
            }
        )
    )    
    Newpassword1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Enter New Password"
            }
        )
    )        
    Newpassword2=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Confirm Password"
            }
        )
    ) 
    class Meta:
        fields=('oldpassword','Newpassword1','Newpassword2')
        model=User