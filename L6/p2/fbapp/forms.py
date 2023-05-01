from django import forms 
class FbForm(forms.Form):
    name = forms.CharField()
    feedback = forms.CharField()