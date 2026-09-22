from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from orders.models import Order
from .forms import CustomUserCreationForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"مرحباً بك مجدداً {username}!")

                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('accounts:profile')
        else:
            messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيحة.")
    else:
        form = AuthenticationForm()
        
    return render(request, 'accounts/login.html', {'form': form})

def register_view(request):

    if request.user.is_authenticated:
        return redirect('accounts:profile')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            messages.success(request, "تم إنشاء حسابك بنجاح! مرحباً بك.")
            return redirect('accounts:profile')
        else:
            messages.error(request, "يرجى تصحيح الأخطاء الموضحة أدناه.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form })


@login_required
def profile_view(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    return render(request, 'accounts/profile.html', {
        'orders': orders
    })

@login_required
def order_detail_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    return render(request, 'accounts/order_detail.html', {
        'order': order
    })