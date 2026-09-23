from django.shortcuts import redirect, get_object_or_404 ,render 
from products.models import Product
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib import messages

@require_POST

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    override = False
    if form.is_valid():
        cd = form.cleaned_data
        override = cd['override']
        cart.add(
            product=product,
            quantity=cd['quantity'],
            override_quantity=override
        )
    else:
        override_param = request.POST.get('override', 'False') == 'True'
        quantity = int(request.POST.get('quantity', 1))
        cart.add(product=product, quantity=quantity, override_quantity=override_param)
        override = override_param

    if not override:
        messages.success(request, f'تمت إضافة "{product.name}" إلى سلة التسوق بنجاح!')
    
    return redirect(request.META.get('HTTP_REFERER', 'products:product_list'))

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True
        })
    return render(request, 'cart/detail.html', {'cart': cart})

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')