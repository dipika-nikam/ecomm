from django import forms
from .models import Add_product

class Productsform(forms.ModelForm):
    class Meta:
        model = Add_product
        fields = '__all__'
        exclude=['user']
