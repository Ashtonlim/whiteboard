from django import forms
from .models import Course

class q(forms.Form):
    q = forms.CharField(label=False, required=False, max_length=100)
    course_filter = forms.ModelChoiceField(queryset=Course.objects.all(), required=False, label=False, to_field_name="pk")
    class Meta:
        model = Course