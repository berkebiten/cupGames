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
    date_of_birth = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.DateInput, label='Date of Birth',
                                    required=True)

    class Meta:
        model = Account
        fields = ('username', 'password', 'email', 'gender', 'date_of_birth',)


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Account
        fields = ('username', 'password')
