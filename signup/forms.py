
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class SignUpForm(UserCreationForm):
    hint = forms.CharField()
    captcha = CaptchaField()
    
    class Meta:
        model = User
        fields = ('username', 'email', 'hint', 'password1', 'password2', )
