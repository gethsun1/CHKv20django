# inventory/models.py

from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    cost_per_item = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    quantity_in_stock = models.IntegerField(null=False, blank=False)
    quantity_sold = models.IntegerField(null=False, blank=False)
    total_sales = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    stock_date = models.DateField(auto_now_add=True)
    last_sales_date = models.DateField(auto_now=True)
    product_image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def save(self, *args, **kwargs):
        # Calculate total_sales automatically when saving the object
        self.total_sales = self.cost_per_item * self.quantity_sold
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
