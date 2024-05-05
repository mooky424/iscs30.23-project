from django import forms

from .models import Product


class TransactionForm(forms.Form):
    amount = forms.IntegerField(min_value=0)
