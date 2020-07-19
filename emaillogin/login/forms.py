from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class Signupform(forms.ModelForm):
	
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'password' )

class Signinform(forms.Form):
	
	email = forms.EmailField()
	password = forms.CharField()