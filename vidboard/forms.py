from django import forms
from .models import Course

bootstrapInputClass = 'form-control mb-2 mr-sm-2'
bootstrapChoiceClass = 'custom-select my-1 mr-sm-2'
class q(forms.Form):
    q = forms.CharField(label=False, required=False, max_length=100, widget=forms.TextInput(attrs={'class': bootstrapInputClass, 'placeholder': 'Search Videos'}))
    course_filter = forms.ModelChoiceField(queryset=Course.objects.all(), required=False, label=False, widget=forms.Select(attrs={'class':bootstrapChoiceClass}))
    class Meta:
        model = Course