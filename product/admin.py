from django.contrib import admin
from .models import Tag, Author, Product, Gender, Category, Discount,SalesProduct,NewCollection


admin.site.register([Tag, Author, Gender, Category, Discount,Product])



@admin.register(SalesProduct)
class SalesProductAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(discount__name__gt=0)
    
@admin.register(NewCollection)
class NewCollectionAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(discount__name__isnull=True)
    

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
    
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         return qs.filter(discount__name__gt=0)
    