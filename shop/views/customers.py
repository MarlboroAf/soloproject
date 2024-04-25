from django.contrib import messages
from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from shop.forms import CustomerForm


@login_required
def customer_list(request):
    user = request.user
    if user.is_authenticated & user.is_staff:
        users = User.objects.all()
        return render(request, 'shop/customer_list.html', {'users' : users})
    else:
        return redirect('shop:login')

@login_required
def customer_detail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'shop/customer_detail.html', {'user' : user})


def customer_edit(request,id):
    user = get_object_or_404(User, id=id)
    if request.user.is_authenticated & request.user.is_staff:
        pass
    elif not request.user.is_superuser and request.user != user:
        return redirect('shop:product_list')
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('shop:customer_detail', id=id)

        else:
            form = CustomerForm(instance=user)
    return render(request, 'shop/customer_edit.html', {'form': form, 'user': user})


def customer_delete(request,id):
    if request.method == "POST":
        customer = get_object_or_404(User, id=id)
        customer.delete()
        return redirect('shop:customer_list')