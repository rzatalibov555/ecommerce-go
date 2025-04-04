from django.shortcuts import render
from django.db.models import Q, F, Value, CharField, FloatField
from django.db.models.functions import Concat, Cast, Coalesce


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