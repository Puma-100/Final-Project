from django import forms
from django.core import validators
from .models import Text

class TextForSentiment(forms.ModelForm):

    text = forms.CharField(label="",
                           widget=forms.Textarea( attrs={'style': 'width: 75%; height: 75%; resize: none',
                                                         'class': 'form-group'}))

    botcatcher = forms.CharField(required=False,
                                  widget=forms.HiddenInput,
                                  validators = [validators.MaxLengthValidator(0)])

    class Meta:
        model = Text
        fields = ('text', )
