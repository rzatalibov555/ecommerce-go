from django.contrib import admin
from .models import Tag, Author, Product, Gender, Category, Discount, SalesProduct, NewCollection, AuthorProfile
from django.utils.html import format_html
from .models import ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ['preview']

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:100px;" />', obj.image.url)
        return "-"

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_preview', 'time_create', 'time_update', 'status','category']
    list_editable = ["status"]
    list_display_links = ["name"]
    list_filter = ['status']
    search_fields = ['name']
    
    inlines = [ProductImageInline]

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<a href="{}" target="_blank"><img src="{}" style="width: 100px; height: 70px; object-fit:cover;" /></a>',
                obj.image.url,
                obj.image.url
            )
        return "No Image"






@admin.register(SalesProduct)
class SalesProductAdmin(admin.ModelAdmin):
    list_display = ("name","price")
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
    


admin.site.register(Product, ProductAdmin)
admin.site.register([Tag, Author, Gender, Category, Discount, AuthorProfile])

# admin.site.register(Product, ProductAdmin)
# admin.site.register([Tag, Author, Gender, Category, Discount, AuthorProfile, ProductAdmin])