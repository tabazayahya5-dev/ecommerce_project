from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import render, get_object_or_404

def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)

    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request , slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'products/product_detail.html', {'product': product})