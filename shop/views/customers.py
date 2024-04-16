from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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

