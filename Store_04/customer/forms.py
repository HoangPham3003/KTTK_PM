from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='User name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'my-3 border border-danger border-top-0 border-end-0 border-start-0 form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'my-3 border border-danger border-top-0 border-end-0 border-start-0 form-control'}))


class SignupFormAccount(forms.Form):
    username = forms.CharField(label='User name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'my-3 border border-danger border-top-0 border-end-0 border-start-0 form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'my-3 border border-danger border-top-0 border-end-0 border-start-0 form-control'}))
    password_retyped = forms.CharField(label='Retype password', widget=forms.PasswordInput(attrs={'placeholder': 'Retype password', 'class': 'my-3 border border-danger border-top-0 border-end-0 border-start-0 form-control'}))


class SignupFormInformation(forms.Form):
    firstname = forms.CharField(label='First name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First name', 'class': 'my-3 border border-danger border-top-0 border-end-0 border-start-0 form-control'}))
    midname = forms.CharField(label='Mid name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Mid name', 'class': 'my-3 border border-danger border-top-0 border-end-0 border-start-0 form-control'}))
    lastname = forms.CharField(label='Last name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last name', 'class': 'my-3 border border-danger border-top-0 border-end-0 border-start-0 form-control'}))
    house_number = forms.CharField(label='House number', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'House number', 'class': 'my-3 border border-danger border-top-0 border-end-0 border-start-0 form-control'}))
    street = forms.CharField(label='Street', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Street', 'class': 'my-3 border border-danger border-top-0 border-end-0 border-start-0 form-control'}))
    district = forms.CharField(label='District', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'District', 'class': 'my-3 border border-danger border-top-0 border-end-0 border-start-0 form-control'}))
    city = forms.CharField(label='City', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'City', 'class': 'my-3 border border-danger border-top-0 border-end-0 border-start-0 form-control'}))
    country = forms.CharField(label='Country', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Country', 'class': 'my-3 border border-danger border-top-0 border-end-0 border-start-0 form-control'}))
    dob = forms.DateField(label='Date of birth', widget=forms.DateInput(attrs={'placeholder': 'Date of birth', 'class': 'my-3 border border-danger border-top-0 border-end-0 border-start-0 form-control'}))
    phone = forms.CharField(label='Phone number', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Phone number', 'class': 'my-3 border border-danger border-top-0 border-end-0 border-start-0 form-control'}))


class ChangePwdForm(forms.Form):
    old_password = forms.CharField(label='Old password', widget=forms.PasswordInput(attrs={'placeholder': 'Old password', 'class': 'my-3 border border-danger border-top-0 border-end-0 border-start-0 form-control'}))
    new_password = forms.CharField(label='New password', widget=forms.PasswordInput(attrs={'placeholder': 'New password', 'class': 'my-3 border border-danger border-top-0 border-end-0 border-start-0 form-control'}))
    new_password_retyped = forms.CharField(label='Retype new password', widget=forms.PasswordInput(attrs={'placeholder': 'Retype new password', 'class': 'my-3 border border-danger border-top-0 border-end-0 border-start-0 form-control'}))