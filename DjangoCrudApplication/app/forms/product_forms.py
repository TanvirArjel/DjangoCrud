from app.models.product import Product
from django import forms

class ProductForm(forms.ModelForm):
    product_name = forms.CharField(error_messages={'required': 'Product Name is required!'},
                                   widget=forms.TextInput({'class': 'form-control','placeholder': 'Enter product name'}))
    price = forms.DecimalField(error_messages={'required': 'Product price is required!'},
                                   widget=forms.TextInput({'class': 'form-control','placeholder': 'Enter product price'}))
    quantity = forms.IntegerField(error_messages={'required': 'Product quantity is required!'},
                                   widget=forms.NumberInput({'class': 'form-control','placeholder': 'Enter product quantity'}))
    class Meta:
        model = Product
        fields = '__all__'