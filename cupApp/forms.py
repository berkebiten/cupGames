from django import forms
from .models import Account

GENDER_CHOICES = [
    ("F", "Female"),
    ("M", "Male"),
    ("O", "Other")
]

class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput, label='Username', required=True)
    email = forms.CharField(widget=forms.EmailInput, label='Email', required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label='Password', required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender', required=True)
    gender.widget.attrs.update({'class':'genderChoice'})


    class Meta:
        model = Account
        fields = ('username', 'password', 'email', 'gender',)


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Account
        fields = ('username', 'password')
