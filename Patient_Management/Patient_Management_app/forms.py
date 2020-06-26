from django import forms
from Patient_Management_app.models import UserProfileInfo
from django.contrib.auth.models import User
import uuid

YEARS = [x for x in range(1947,2020)]

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):
	birth_date = forms.DateField(help_text='Required.',widget=forms.SelectDateWidget(years=YEARS))
	userid = forms.IntegerField()
	class Meta():
		model = UserProfileInfo
		fields = ('first_name', 'last_name','birth_date')


