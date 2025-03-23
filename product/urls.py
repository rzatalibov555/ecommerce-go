from django.contrib import admin
from django.urls import path    
from .views import *

urlpatterns = [
    path('', index),
    path('home', index, name='index'),
    path('allProducts', allProducts, name='allProducts'),
    path('product_detail', product_detail, name='product_detail')
    
]