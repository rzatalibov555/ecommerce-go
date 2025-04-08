from django.db import models

# Create your models here.

# GENDER = (
#     ("male", "male"),
#     ("female", "female"),
#     ("other", "other"),
# )


class Tag(models.Model):
    name = models.CharField(max_length=300, verbose_name="Ad")
    status = models.BooleanField(default=True, verbose_name="Status")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Yaranma tarixi")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Yenilənmə tarixi")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ad")
    icon = models.FileField(upload_to="category", verbose_name="Şəkil")
    status = models.BooleanField(default=True, verbose_name="Status")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Yaranma tarixi")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Yenilənmə tarixi")

    def __str__(self):
        return self.name

class Gender(models.Model):
    gender = models.CharField(max_length=300, verbose_name="Ad")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Yaranma tarixi")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Yenilənmə tarixi")

    def __str__(self):
        return self.gender

class Author(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Cinsi")
    name = models.CharField(max_length=300, verbose_name="Ad")
    surname = models.CharField(max_length=300, verbose_name="Soyad")
    age  = models.PositiveIntegerField(verbose_name="Yaş")
    birthday = models.DateField(verbose_name="Doğum tarixi")
    status = models.BooleanField(default=True, verbose_name="Status")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Yaranma tarixi")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Yenilənmə tarixi")
    

    def __str__(self):
        return self.name

class Product(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=300, verbose_name="Ad")
    price = models.FloatField(verbose_name="Qiymət")
    tax_price = models.FloatField(blank=True, null=True, verbose_name="Tax qiymət")
    discount_price = models.FloatField(blank=True, null=True, verbose_name="Endirimli qiymət")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="category", null=True)
    image = models.ImageField(upload_to="product/%Y/%m/%d/", verbose_name="Şəkİl")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Tag")
    coupon = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(default=True, verbose_name="Status")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Yaranma tarixi")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Yenilənmə tarixi")
    

    def __str__(self):
        return self.name