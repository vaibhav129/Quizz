from django import  forms
from .models import *

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = ('is_selected',)