from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from shop.forms import BasketAddProductForm, ProductForm
from shop.models import Product
from django.core.paginator import Paginator
def product_list(request):
    all_products = Product.objects.all()  # Assuming Product is your model
    if request.GET.get('q')!= None:
        all_products = all_products.filter(name__icontains=request.GET.get('q'))
    paginator = Paginator(all_products, 50)  # Show 50 products per page

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'shop/merchandise_list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    basket_product_form = BasketAddProductForm()
    return render(request, 'shop/merchandise_detail.html', {'product' : product, 'basket_product_form': basket_product_form})

def product_new(request):
    if request.method=="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_date = timezone.now()
            product.save()
            return redirect('shop:product_detail', id=product.id)
    else:
        form = ProductForm()
    return render(request, 'shop/merchandise_edit.html', {'form': form})

def product_edit(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method=="POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_date = timezone.now()
            product.save()
            return redirect('shop:product_detail', id=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/merchandise_edit.html', {'form': form})

def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    deleted = request.session.get('deleted', 'empty')
    request.session['deleted'] = product.name
    product.delete()
    return redirect('shop:product_list' )
