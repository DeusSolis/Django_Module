from django.forms import ModelForm
from .models import Product, Purchase, PurchaseReturns


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'quantity_in_stock', 'image')


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ('quantity_of_products',)


class PurchaseReturnForm(ModelForm):
    class Meta:
        model = PurchaseReturns
        fields = []