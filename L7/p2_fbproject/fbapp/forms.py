from django import forms
from .models import FbModel
class FbForm(forms.ModelForm):
    feedback = forms.CharField(widget=forms.Textarea(attrs={"rows":5,"cols":22,"style":"resize:none"}))
    class Meta:
        model = FbModel
        fields = ["name","feedback"]