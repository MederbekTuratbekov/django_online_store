# создовайтеткенде, обновляйтеткенде пайда болчуу форма
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'product_name', 'price', 'year', 'product_type', 'description', 'image']