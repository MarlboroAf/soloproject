from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Customer


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=50)
    address = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 
        'address', 'first_name', 'last_name', )

class ProductForm (forms.ModelForm):
    name= forms.CharField(max_length=200)

    class Meta:
        model = Product
        fields = ('name','price',)

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class BasketAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)

class CustomerForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', )

