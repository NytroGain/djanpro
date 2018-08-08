from django import forms
from .models import UserEmail

class TestForm(forms.ModelForm):
    class Meta:
        model = UserEmail
        fields = ('first_name','last_name','email',)