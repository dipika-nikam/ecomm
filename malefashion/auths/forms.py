from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import NewUser
class Sign_up_form(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ['username','email','first_name','last_name','password1','password2','user_type']

class Login_form(AuthenticationForm):
    pass


