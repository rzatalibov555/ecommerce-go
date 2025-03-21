from django.contrib import admin
from django.urls import path    
from .views import *

urlpatterns = [
    path('', index),
    path('home', index, name='index'),
    path('shopgrid3', shopgrid3, name='shopgrid3'),
    path('product_detail', product_detail, name='product_detail')
    
]