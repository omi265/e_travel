from django.contrib.auth.models import User
from django import forms
from .models import Customer

class Updateuserinfo(forms.ModelForm):
    email = forms.EmailField()
    email.widget.attrs.update({
        'class': 'form-control'
    })
    class Meta:
        model=User
        fields=['username','email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            # 'email': forms.EmailField(attrs={'class': 'form-control'})
        }

class Updatecustomerinfo(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','phone', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }