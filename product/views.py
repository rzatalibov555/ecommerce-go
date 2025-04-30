from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.db.models import Q, F, Value, CharField, FloatField, ExpressionWrapper, Count
from django.db.models.functions import Concat, Cast, Coalesce, Round


from product.forms import ProductForm

from product.models import *


def index(request):
    context = {
        "nav_cat":True,
        "category": Category.objects.annotate(
            product_count = Count("products")
        ).order_by('-time_create')[:10],
        "product": Product.objects.annotate(
            tax= Coalesce(F("tax_price"), 0, output_field=FloatField()),
            discount_p=Coalesce(F("discount__name"),0, output_field=FloatField())
            ).annotate(
                total_price = F("price") *(1- F("discount_p") / 100) + F("tax")
            ),

            # total_price=ExpressionWrapper(
            #     # (F("price") * (1 - Coalesce(F("discount__name"), 0) / 100)) + Coalesce(F("tax_price"), 0),
            #     # output_field=FloatField()
            # )
        
        # "product_discount": Product.objects.annotate(
        #  discount_price=ExpressionWrapper(
        #             (F("price")-F("discount_price"))
        #         )
        #     )

        "discount_products": Product.objects.annotate(
            tax= Coalesce(F("tax_price"), 0, output_field=FloatField()),
            discount_p=Coalesce(F("discount__name"),0, output_field=FloatField())
            ).annotate(
                total_price = F("price") *(1- F("discount_p") / 100) + F("tax")
            ).filter(discount__name__gt=0),


        "last_products": Product.objects.annotate(
            tax= Coalesce(F("tax_price"), 0, output_field=FloatField()),
            discount_p=Coalesce(F("discount__name"),0, output_field=FloatField())
            ).annotate(
                total_price = Round(F("price") *(1- F("discount_p") / 100) + F("tax"),2
                )
            ).order_by('-id')[:5]
            
    }
    

    # print(context)
    return render(request, "product/index.html", context)

def allProducts(request):
    return render(request, "product/shop-grid-3.html")

def product_detail(request):
    return render(request, "product/shop-single.html")


def pageNotFound(request, exception):
    return HttpResponseNotFound("UPSSS! Sehife tapilmadi")

def all_categories(request):
    context= {
        "nav_cat":False,
        "category_all":Category.objects.annotate(cat_count=Count("products")).filter(status=True)
    }

    return render(request, "product/category.html", context)

def category_products(request,c_id):
    try:
        category = Category.objects.get(id=c_id)
    except:
        raise Http404()
    
    category_products = Product.objects.filter(status=True).filter(category=c_id).annotate(
            tax= Coalesce(F("tax_price"), 0, output_field=FloatField()),
            discount_p=Coalesce(F("discount__name"),0, output_field=FloatField())
            ).annotate(total_price = Round(F("price") *(1- F("discount_p") / 100) + F("tax"),2))
    
    categories = Category.objects.annotate(product_count=Count("products"))[:10]

    context={
        "category_products": category_products,
        "category_products_count": category_products.count(),
        "category": category,
        "categories": categories,
    
    }
    return render(request, "product/shop-grid.html",context)

def product_create_view(request):

    # request => method: GET,  -datani getir
    # request => method: POST, -datani gonder db-ya
    # context["form"] = form
    
    context = {}
    form = ProductForm()

    if request.method == "POST":
        # print(request.POST)
        # name = request.POST.get("name")
        form = ProductForm(data=request.POST)
        # form = ProductForm(request.POST, request.FILES)
     
        
        if form.is_valid():
            # print(form)
            form.save(commit=True)
            return redirect('product:index')
        else:
            print(form.errors)
            # form = ProductForm()
    else:
        form = ProductForm()
        
    context['form'] = form

    return render(request, "product/vendor-add-product.html", context)













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

# Product.objects.filter(Q(author_id=1) | Q(author__name="Aytac"))



# Annotate

# fullad = Author.objects.annotate(
#     full_name=Concat(
#         F("name"), Value(" "), F("surname"), Value(" -> "), Cast(F("age"), CharField())
#     )
# )


# from django.db.models import Q, F, Value, CharField, FloatField
# from django.db.models.functions import Concat, Cast, Coalesce

# cavab = Product.objects.annotate(
#     tax=Coalesce(F("tax_price"), 0, output_field=FloatField()),
#     discount=Coalesce(F("discount_price"), 0, output_field=FloatField())
# )


# from django.db.models import F, Value, FloatField
# from django.db.models.functions import Coalesce

# cavab = Product.objects.annotate(
#     tax=Coalesce(F("tax_price"), Value(0.0), output_field=FloatField()),
#     discount=Coalesce(F("discount_price"), Value(0.0), output_field=FloatField())
# )

# list(cavab.values("name", "tax", "discount"))