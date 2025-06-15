from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'user_type',
                  'profile_pic', 'address_line1', 'city', 'state', 'pincode', 'password1', 'password2']
