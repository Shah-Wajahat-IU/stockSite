import imp
from django import forms
from .models import Ticker

class StockForm(forms.ModelForm):
    class Meta:
        model=Ticker
        fields=["ticker"]