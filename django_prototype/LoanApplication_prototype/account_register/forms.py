from django import forms
from django.forms import fields

from .models import Account , Personal_Details

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['email','password','repassword']


class Personal_Detail_form(forms.ModelForm):
    class Meta:
        model = Personal_Details
        fields = ['title_face','image_face','title_ID','image_ID']