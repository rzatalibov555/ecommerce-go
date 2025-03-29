from django.shortcuts import render
from django.db.models import Q

def index(request):
    return render(request, "product/index.html")

def allProducts(request):
    return render(request, "product/shop-grid-3.html")

def product_detail(request):
    return render(request, "product/shop-single.html")


# & - AND // VE
# | - OR  // VE YA


# Product.objects.filter(
# +      Q(author_id=1)
# AND    &
# +      Q(author__name="Aytac")
#)

# Product.objects.filter(
# -      Q(author_id=1)
# OR     |
# +      Q(author__name="Aytac")
#)