from django import forms

class loginForm(forms.Form):
    user = forms.CharField()
    pass1 = forms.CharField()