from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from shop.models import Cart, Customer, LineItem, Order, Product
from shop.forms import SignUpForm
from shop.views.basket import Basket

def signup(request):
    """
    View for user registration (signup).
    """
    form = SignUpForm(request.POST)
    if form.is_valid():
        # If the form is valid, save the user and create associated customer
        user = form.save()
        user.refresh_from_db()
        # Update additional fields for the customer
        user.customer.first_name = form.cleaned_data.get('first_name')
        user.customer.last_name = form.cleaned_data.get('last_name')
        user.customer.address = form.cleaned_data.get('address')
        user.save()
        # Log in the user
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    return render(request, 'signup.html', {'form': form})

def payment(request):
    """
    View for processing payment and saving the order.
    """
    basket = Basket(request)
    user = request.user
    customer = get_object_or_404(Customer, user_id=user.id)
    # Create a new order for the customer
    order = Order.objects.create(customer=customer)
    order.refresh_from_db()
    # Create line items for each product in the basket
    for item in basket:
        product_item = get_object_or_404(Product, id=item['product_id'])
        cart = Cart.objects.create(product=product_item, quantity=item['quantity'])
        cart.refresh_from_db()
        line_item = LineItem.objects.create(quantity=item['quantity'], product=product_item, cart=cart, order=order)

    # Clear the basket after processing the order
    basket.clear()
    # Set a session variable to indicate successful purchase
    request.session['deleted'] = 'thanks for your purchase'
    return redirect('shop:product_list')

def purchase(request):
    """
    View for displaying payment page.
    """
    if request.user.is_authenticated:
        user = request.user
        basket = Basket(request)
        return render(request, 'shop/payment.html', {'basket': basket, 'user': user})
    else:
        # Redirect to login page if user is not authenticated
        return redirect('shop:login')
