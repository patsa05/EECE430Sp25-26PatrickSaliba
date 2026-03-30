from django import forms
from .models import VoleyPlayer


class VoleyPlayerForm(forms.ModelForm):
    class Meta:
        model = VoleyPlayer
        fields = ['name', 'date_joined', 'position', 'salary', 'contact_person']
        widgets = {
            'date_joined': forms.DateInput(attrs={'type': 'date'})
        }