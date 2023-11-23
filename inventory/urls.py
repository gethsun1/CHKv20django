
#inventory/urls.py

from django.urls import path
from .views import delete_inventory, inventory_list, per_product_view, add_product, update_inventory

urlpatterns = [
    path("", inventory_list, name="inventory_list"),
    path("per_product/<int:pk>", per_product_view, name="per_product"),
    path("add_inventory/", add_product, name="add_inventory"),
    path("delete/<int:pk>", delete_inventory, name="delete_inventory"),
    path("update/<int:pk>", update_inventory, name="update_inventory"),
]
