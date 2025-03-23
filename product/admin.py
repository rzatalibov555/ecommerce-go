from django.contrib import admin
from .models import Tag, Author, Product


admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Product)
