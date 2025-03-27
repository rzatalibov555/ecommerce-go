from django.contrib import admin
from .models import Tag, Author, Product, Gender


admin.site.register([Tag, Author, Product, Gender])
