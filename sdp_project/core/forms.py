from django import forms
from .models import Sale
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['title', 'description', 'amount', 'seller']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1",)  # Add other fields if needed

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "password")