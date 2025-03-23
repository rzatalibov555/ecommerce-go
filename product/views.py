from django.shortcuts import render


def index(request):
    return render(request, "product/index.html")

def allProducts(request):
    return render(request, "product/shop-grid-3.html")

def product_detail(request):
    return render(request, "product/shop-single.html")


