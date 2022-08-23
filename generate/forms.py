from logging import PlaceHolder
from django import forms

class textinput(forms.Form):
    inp=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Input'}))
