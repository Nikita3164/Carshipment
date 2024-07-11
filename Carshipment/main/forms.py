from django import forms
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'phone_number', 'email', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'formField', 'placeholder': 'Имя'}),
            'phone_number': forms.TextInput(attrs={'class': 'formField', 'type': 'number', 'placeholder': 'Телефон'}),
            'email': forms.TextInput(attrs={'class': 'formField', 'type': 'email', 'placeholder': 'Электронная почта'}),
            'comment': forms.Textarea(attrs={'class': 'formField', 'placeholder': 'Комментарий'}),
        }


class RequestFormExtended(forms.ModelForm):
    class Meta:
        CHOICES = [('Покупка авто', 'Покупка авто'), ('Продажа авто', 'Продажа авто'), ('Сотрудничество', 'Сотрудничество')]
        model = Request
        fields = ['name', 'subject', 'phone_number', 'email', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'formField', 'placeholder': 'Имя'}),
            'subject': forms.Select(choices=CHOICES),
            'phone_number': forms.TextInput(attrs={'class': 'formField', 'type': 'number', 'placeholder': 'Телефон'}),
            'email': forms.TextInput(attrs={'class': 'formField', 'type': 'email', 'placeholder': 'Электронная почта'}),
            'comment': forms.Textarea(attrs={'class': 'formField', 'placeholder': 'Комментарий'}),
        }