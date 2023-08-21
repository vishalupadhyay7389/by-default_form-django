from django import forms

class StudentRegistraion(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()