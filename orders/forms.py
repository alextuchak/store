from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов'}))
    cell_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': '+7 XXX-XXX-XX-XX'}))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Россия, Москва, ул. Ленина, дом 1, кв. 1'
    }))

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'cell_phone', 'address')
