from django.contrib import admin
from .models import Tag, Author, Product, Gender, Category, Discount


admin.site.register([Tag, Author, Product, Gender, Category, Discount])
