from django import forms
from .models import Product, Order

class ProductAdd(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity']
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'orderquantity']