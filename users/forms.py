from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm password')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'confirm_password']

    def clean_confirm_password(self):
        data = self.cleaned_data
        if data['password']!= data['confirm_password']:
            raise forms.ValidationError('Passwords do not match.')
        return data['confirm_password']


