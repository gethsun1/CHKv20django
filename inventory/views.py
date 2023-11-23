# inventory/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Inventory
from .forms import AddInventoryForm, UpdateInventoryForm
from django.urls import reverse_lazy


INVENTORY_LIST_URL = reverse_lazy('inventory_list')


@login_required
def inventory_list(request):
    # Retrieve all inventories
    inventories = Inventory.objects.all()
    
    # Prepare context for rendering the template
    context = {"title": "Inventory List", "inventories": inventories}
    
    # Render the template with the context
    return render(request, "inventory/inventory_list.html", context=context)

@login_required
def per_product_view(request, pk):
    # Retrieve a specific inventory based on the primary key (pk)
    inventory = get_object_or_404(Inventory, pk=pk)
    
    # Prepare context for rendering the template
    context = {"inventory": inventory}
    
    # Render the template with the context
    return render(request, "inventory/per_product.html", context=context)


@login_required
def add_product(request):
    if request.method == "POST":
        add_form = AddInventoryForm(request.POST, request.FILES)
        
        if add_form.is_valid():
            new_inventory = add_form.save(commit=False)
            
            # Check if an inventory item with the same name already exists
            existing_inventory = Inventory.objects.filter(name=new_inventory.name).first()
            
            if existing_inventory:
                # Update existing inventory item
                existing_inventory.quantity_in_stock = F('quantity_in_stock') + new_inventory.quantity_in_stock
                existing_inventory.quantity_sold = F('quantity_sold') + new_inventory.quantity_sold
                existing_inventory.cost_per_item = new_inventory.cost_per_item
                existing_inventory.last_sales_date = timezone.now()
                existing_inventory.save()
            else:
                # Create a new inventory item
                new_inventory.sales = new_inventory.cost_per_item * new_inventory.quantity_sold
                new_inventory.save()
            
            return redirect(INVENTORY_LIST_URL)
    else:
        add_form = AddInventoryForm()
    
    return render(request, "inventory/inventory_add.html", {"form": add_form})


@login_required
def delete_inventory(request, pk):
    # Retrieve the inventory to be deleted
    inventory = get_object_or_404(Inventory, pk=pk)
    
    # Delete the inventory
    inventory.delete()
    
    # Redirect to the inventory list using the URL pattern name
    return redirect('inventory_list')

@login_required
def update_inventory(request, pk):
    # Retrieve the inventory to be updated
    inventory = get_object_or_404(Inventory, pk=pk)
    
    if request.method == "POST":
        # If the form is submitted, process the data
        update_form = UpdateInventoryForm(data=request.POST, instance=inventory)
        
        if update_form.is_valid():
            # If the form is valid, save the updated inventory
            update_form.save()
            
            # Redirect to the inventory list using the URL pattern name
            return redirect('inventory_list')
    else:
        # If it's a GET request, display the form
        update_form = UpdateInventoryForm(instance=inventory)
    
    # Render the template with the form
    context = {"form": update_form}
    return render(request, "inventory/inventory_update.html", context=context)
