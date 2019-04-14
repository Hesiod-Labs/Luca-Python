from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import Profile


# Form for the creation of the user
class UserRegisterForm(UserCreationForm):
    # The user's email
    email = forms.EmailField()
    # The user's first name
    first_name = forms.CharField(max_length=30, required=True)
    # The user's last name
    last_name = forms.CharField(max_length=30, required=True)
    # The user's university
    university = forms.CharField(max_length=50, required=True)
    # The user's major
    major = forms.CharField(max_length=20, required=False)

    # Specifies the model which will be impacted by the form
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'university', 'major', 'password1', 'password2']


# Form for updating the user sections of the profile
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    # The user model will be impacted
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


# Form for updating the profile sections of the profile
class ProfileUpdateForm(forms.ModelForm):
    university = forms.CharField(max_length=50, required=True)
    major = forms.CharField(max_length=20, required=False)

    # The Profile model will be impacted
    class Meta:
        model = Profile
        fields = ['image', 'university', 'major']
