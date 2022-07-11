from django import forms
from .models import Jweet


class JweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder":"Jweet somethings...",
                "class":"textarea is-success is-medium",
            }
        ),
        label="", 
    )


    class Meta:
        model = Jweet
        exclude = ('user', )
