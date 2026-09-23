from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'category': 'الفئة',
            'name': 'اسم المنتج',
            'slug': 'الرابط اللطيف (Slug)',
            'image': 'صورة المنتج',
            'description': 'الوصف',
            'price': 'السعر',
            'available': 'متوفر في المخزون',
        }
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل اسم المنتج'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'مثال: iphone-15-pro'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }