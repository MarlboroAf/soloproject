from django.urls import path, include
import django.contrib.auth.urls
from . import views
from shop.views import merchandise, customers, orders, basket, general

app_name = 'shop'

urlpatterns = [
    path('', views.merchandise.product_list, name='product_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('basket_add/<int:product_id>/', views.basket.basket_add, name='basket_add'),
    path('basket_remove/<int:product_id>/', views.basket.basket_remove, name='basket_remove'),
    path('basket_detail/', views.basket.basket_detail, name='basket_detail'),
    path('signup/', views.general.signup, name='signup'),
    path('customer_list', views.customers.customer_list, name='customer_list'),
    path('customer/<int:id>/', views.customers.customer_detail, name='customer_detail'),
    path('order_list/', views.orders.order_list, name='order_list'),
    path('order/<int:id>/', views.orders.order_detail, name='order_detail'),
    path('payment/', views.general.payment, name='payment'),
    path('product_list/', views.merchandise.product_list, name='product_list'),
    path('product/<int:id>/', views.merchandise.product_detail, name='product_detail'),
    path('product_new/', views.merchandise.product_new, name='product_new'),
    path('product/<int:id>/edit/', views.merchandise.product_edit, name='product_edit'),
    path('product/<int:id>/delete/', views.merchandise.product_delete, name='product_delete'),
    path('purchase/', views.general.purchase, name='purchase'),
    path('customer_edit/<int:id>/', views.customers.customer_edit, name='customer_edit'),
    path('customer_delete/<int:id>/', views.customers.customer_delete, name='customer_delete')
]
