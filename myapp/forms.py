from django import forms 
from myapp.models import*
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
 

class contectform(forms.ModelForm):
    class Meta:
       fields='__all__'
       model=contect 

class registrationform(UserCreationForm):
    class Meta:
       fields=('first_name','last_name','username','email','password1','password2')
       model=User 