from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='User name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'border border-danger border-top-0 border-end-0 border-start-0 form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'border border-danger border-top-0 border-end-0 border-start-0 form-control'}))
