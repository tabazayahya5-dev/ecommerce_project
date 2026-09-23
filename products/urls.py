from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    
    path('add/', views.product_create, name='product_create'),
    path('<int:id>/edit/', views.product_update, name='product_update'),
    path('<int:id>/delete/', views.product_delete, name='product_delete'),

    path('category/add/', views.category_create, name='category_create'),
    path('category/<int:id>/edit/', views.category_update, name='category_update'),
    path('category/<int:id>/delete/', views.category_delete, name='category_delete'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),

    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]