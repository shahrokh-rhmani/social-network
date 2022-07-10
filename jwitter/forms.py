from django import forms
from .models import Jweet


class JweetForm(forms.ModelForm):
    body = forms.CharField(required=True)

    class Meta:
        model = Jweet
        exclude = ('user', )
