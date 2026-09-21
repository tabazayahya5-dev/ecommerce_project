from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

@login_required
def order_create(request):
    cart = Cart(request)
    
    if len(cart) == 0:
        return redirect('products:product_list')

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )

            cart.clear()

            return render(request, 'order/created.html', {'order': order})
    else:
        form = OrderCreateForm()

    return render(request, 'order/create.html', {
        'cart': cart,
        'form': form
    })