from django import forms
from .models import PasswordEntry

class PasswordEntryForm(forms.ModelForm):
    class Meta:
        model = PasswordEntry
        fields = ['website', 'username']
        widgets = {
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Password"
    )
