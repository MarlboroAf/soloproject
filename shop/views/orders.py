from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from shop.models import LineItem, Order

def order_list(request):
    """
    View for displaying a list of orders.
    """
    # Fetch all orders from the database
    orders = Order.objects.all()
    return render(request, 'shop/order_list.html', {'orders': orders})

def order_detail(request, id):
    """
    View for displaying details of a specific order.
    """
    # Fetch the order with the provided id or return 404 if not found
    order = get_object_or_404(Order, id=id)
    # Fetch the customer associated with the order
    customer = order.customer
    # Fetch the user associated with the customer
    user = get_object_or_404(User, id=customer.pk)
    # Fetch all line items associated with the order
    line_items = LineItem.objects.filter(order_id=order.id)
    return render(request, 'shop/order_detail.html', {'order': order, 'user': user, 'line_items': line_items})