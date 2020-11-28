from django.contrib.auth.models import User
from django import forms
from .models import Customer

class Updateuserinfo(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']

class Updatecustomerinfo(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','phone', 'email']