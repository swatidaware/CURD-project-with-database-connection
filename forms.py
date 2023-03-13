from django import forms
from .models import User

class StudentRegitaion(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']