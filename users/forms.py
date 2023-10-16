from django import forms

class CustomUserCreationForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

class CustomUserLoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)