from django import forms


class UserLoginForm(forms.Form):
    """ Forms to be used by login user """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)