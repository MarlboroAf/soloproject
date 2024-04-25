from django.contrib import messages
from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from shop.forms import CustomerForm


@login_required
def customer_list(request):
    """
    View for displaying a list of customers.
    """
    user = request.user
    if user.is_authenticated & user.is_staff:
        # Fetch all users from the database
        users = User.objects.all()
        return render(request, 'shop/customer_list.html', {'users' : users})
    else:
        # Redirect to the login page if the user is not staff or not authenticated
        return redirect('shop:login')

@login_required
def customer_detail(request, id):
    # Fetch the user with the provided id or return 404 if not found
    user = get_object_or_404(User, id=id)
    return render(request, 'shop/customer_detail.html', {'user' : user})

def customer_edit(request, id):
    # Fetch the user with the provided id or return 404 if not found
    user = get_object_or_404(User, id=id)
    if request.user.is_authenticated & request.user.is_staff:
        pass
    elif not request.user.is_superuser and request.user != user:
        # Redirect to the product list page if the user is not staff or not the same as the user being edited
        return redirect('shop:product_list')
    if request.method == 'POST':
        # Process form submission
        form = CustomerForm(request.POST, instance=user)
        if form.is_valid():
            # Save the form if it's valid
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('shop:customer_detail', id=id)
        else:
            form = CustomerForm(instance=user)
    return render(request, 'shop/customer_edit.html', {'form': form, 'user': user})

def customer_delete(request, id):
    if request.method == "POST":
        # Fetch the customer with the provided id or return 404 if not found
        customer = get_object_or_404(User, id=id)
        customer.delete()
        return redirect('shop:customer_list')