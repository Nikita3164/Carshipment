from django import forms
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Телефон'}),
        }


class RequestFormExtended(forms.ModelForm):
    class Meta:
        CHOICES = [('1', 'Покупка автом'), ('2', 'Продажа авто'), ('3', 'Сотрудничество')]
        model = Request
        fields = ['name', 'subject', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'subject': forms.Select(choices=CHOICES),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Телефон'}),
        }