from django.shortcuts import render
from .models import Category, Product

def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)

    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'products/product_list.html', context)