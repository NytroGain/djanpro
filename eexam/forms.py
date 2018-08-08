from django import forms
from .models import UserEmail

class TestForm(forms.ModelForm):
    class Meta:
        model = UserEmail
        fields = ('email',)