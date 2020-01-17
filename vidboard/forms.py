from django import forms

class q(forms.Form):
    q = forms.CharField(label=False, required=False, max_length=100)