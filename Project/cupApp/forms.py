from django import forms
from .models import Account


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('username', 'password', 'email', 'gender', 'date_of_birth',)


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Account
        fields = ('username', 'password')
