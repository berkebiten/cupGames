from django import forms
from .models import Account

GENDER_CHOICES = [
    ("F", "Female"),
    ("M", "Male"),
    ("O", "Other")
]


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput, label='Username', required=True, min_length=6, max_length=20,
                               help_text='between 6-20 characters.')
    email = forms.CharField(widget=forms.EmailInput, label='Email', required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label='Password', required=True, min_length=8, max_length=20,
                               help_text='between 8-20 characters.')
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender', required=True)
    gender.widget.attrs.update({'class': 'genderChoice'})

    class Meta:
        model = Account
        fields = ('username', 'password', 'email', 'gender',)


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Account
        fields = ('username', 'password')
