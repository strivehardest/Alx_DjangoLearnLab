# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']
        widgets = {
            'bio': forms.Textarea(attrs={'rows':4, 'placeholder':'A little about yourself...'}),
        }
