from django import forms
from .models import Sale
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer', 'description', 'amount', 'seller']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1",)

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "password")