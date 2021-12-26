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
class DateInput(forms.DateInput):
    input_type = 'date'
    
class TimeInput(forms.TimeInput):
    input_type = 'time'
    
class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ["username", "therapistname", "date", "fromtime", "totime", "paymentstatus", "sessionstatus"]
        widgets = {
            'date': DateInput(),
            'totime':TimeInput(),
            'fromtime':TimeInput()
        }
        attrs={'classs': 'form-control'}
        
class DiscussionForm(forms.ModelForm):
    class Meta:
        model = DiscussionModel
        fields = ['info']