from django import forms
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
from django.contrib.auth.models import User


class CaptchaTestModelForm(UserCreationForm):
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'captcha']
        