from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import *


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class DateInput(forms.DateInput):
    input_type = 'date'


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = (
            'name', 'Mobile_no', 'land_ha', 'soil_ph', 'soil_type', 'district', 'location', 'category', 'crop1',
            'crop2', 'user','datOfSow',
            'yield_tons'
        )
        widgets = {'datOfSow':DateInput(),
'user': forms.HiddenInput()}
