from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.db.models import Q, F, Value, CharField, FloatField, ExpressionWrapper, Count
from django.db.models.functions import Concat, Cast, Coalesce

from product.models import *


def index(request):
    context = {
        "category": Category.objects.annotate(
            product_count = Count("products")
        ),
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
      
    }
    

    print(context)
    return render(request, "product/index.html", context)

def allProducts(request):
    return render(request, "product/shop-grid-3.html")

def product_detail(request):
    return render(request, "product/shop-single.html")


def pageNotFound(request, exception):
    return HttpResponseNotFound("UPSSS! Sehife tapilmadi")

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