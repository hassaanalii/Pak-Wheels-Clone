from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CreateUserForm(UserCreationForm):
    phone_number = forms.CharField(max_length=11)
    
    class Meta:
        model = CustomUser  
        fields = ['phone_number', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        
        self.fields['phone_number'].label = 'Phone Number'
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'

class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ['notes', 'rating']