from django.contrib import admin
from django.urls import path    
from .views import *

app_name= "product"

urlpatterns = [
    path('', index),
    path('home', index, name='index'),
    path('allProducts', allProducts, name='allProducts'),
    path('product_detail', product_detail, name='product_detail'),
    path('product_create_view', product_create_view, name='product_create'),
    path('all_categories', all_categories, name='all_categories'),

    path('categories/<int:c_id>', category_products, name='category_products'),
    
    
]