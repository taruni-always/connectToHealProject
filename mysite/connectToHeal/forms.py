from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import ModelForm
from .models import *

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

'''
class createTherapistForm(UserCreationForm):
    aboutMe = forms.CharField(max_length = 1024)
    workExperience = forms.CharField(max_length = 1024)
    pricePerSession = forms.IntegerField()

    class Meta:
        model = Therapist
        fields = ["username", "email", "password1", "password2", "aboutMe", "workExperience", "pricePerSession"]


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
'''

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = DiscussionModel
        fields = ['info']