from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'role', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full name'}),
            'role': forms.TextInput(attrs={'placeholder': 'Role'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }
