from django import forms 
from .models import WnModel

CHOICES = [("job","JOB"),("ms","MS"),("mba","MBA")]
class WnForm(forms.ModelForm):
    options = forms.CharField(widget=forms.RadioSelect(choices=CHOICES),initial="job")
    class Meta:
        model = WnModel()
        fields = ["name","options"]