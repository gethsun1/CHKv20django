#inventory/forms.py

from django import forms
from .models import Inventory

class AddInventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'cost_per_item', 'quantity_in_stock', 'quantity_sold', 'product_image']

class UpdateInventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'cost_per_item', 'quantity_in_stock', 'quantity_sold', 'product_image']
