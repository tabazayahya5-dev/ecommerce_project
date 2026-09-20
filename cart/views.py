from django.shortcuts import redirect, get_object_or_404 ,render 
from products.models import Product
from .cart import Cart

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product) 
    return redirect('products:product_list')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})