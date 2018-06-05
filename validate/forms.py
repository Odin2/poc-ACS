from django import forms

class ValidateForm(forms.Form):
    csv = forms.FileField()
    path = forms.FileField()
