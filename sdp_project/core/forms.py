from django import forms
from .models import Sale

class SaleForm(forms.ModelForm):
    class Meta:
        model  = Sale
        fields = ['date', 'amount', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }