from django import forms
from django.utils import timezone

class GhostPostAddForm(forms.Form):
    body = forms.CharField(max_length=280)
    boast = forms.BooleanField()