from django.contrib.admin.views.decorators import staff_member_required
from .models import Category, Product
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm , CategoryForm
from django.contrib import messages



def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)

    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})



@staff_member_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'تم إضافة المنتج "{product.name}" بنجاح!')
            return redirect('products:product_detail', id=product.id, slug=product.slug)
    else:
        form = ProductForm()
    
    return render(request, 'products/product_form.html', {
        'form': form,
        'title': 'إضافة منتج جديد'
    })

@staff_member_required
def product_update(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'تم تحديث المنتج "{product.name}" بنجاح!')
            return redirect('products:product_detail', id=product.id, slug=product.slug)
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'products/product_form.html', {
        'form': form,
        'product': product,
        'title': 'تعديل المنتج'
    })

@staff_member_required
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product_name = product.name
        product.delete()
        messages.success(request, f'تم حذف المنتج "{product_name}" بنجاح.')
        return redirect('products:product_list')
    
    return render(request, 'products/product_confirm_delete.html', {'product': product})


@staff_member_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'تم إضافة القسم "{category.name}" بنجاح!')
            return redirect('products:product_list')
    else:
        form = CategoryForm()
    return render(request, 'products/category_form.html', {'form': form, 'title': 'إضافة قسم جديد'})

@staff_member_required
def category_update(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'تم تحديث القسم "{category.name}" بنجاح!')
            return redirect('products:product_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'products/category_form.html', {'form': form, 'category': category, 'title': 'تعديل القسم'})

@staff_member_required
def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        category_name = category.name
        category.delete()
        messages.success(request, f'تم حذف القسم "{category_name}" بنجاح.')
        return redirect('products:product_list')
    return render(request, 'products/category_confirm_delete.html', {'category': category})