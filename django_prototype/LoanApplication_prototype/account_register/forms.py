from django import forms
from django.forms import fields

from .models import Account 

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['email','password','repassword']