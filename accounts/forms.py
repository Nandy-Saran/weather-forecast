from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import Profile


class SignUpForm(forms.Form):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email','password1','password2')

        model=Profile
        fields=  ('name','location','mobile','land_ha','soil_ph','soil_type','district','category','crop1','crop2','yield_ton','aadhar')
