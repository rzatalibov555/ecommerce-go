from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=300, verbose_name="Ad")
    status = models.BooleanField(default=True, verbose_name="Status")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Yaranma tarixi")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Yenilənmə tarixi")

    def __str__(self):
        return self.name


class Author(models.Model):
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
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, verbose_name="Ad")
    price = models.FloatField(verbose_name="Qiymət")
    tax_price = models.FloatField(blank=True, null=True, verbose_name="Tax qiymət")
    discount_price = models.FloatField(blank=True, null=True, verbose_name="Endirimli qiymət")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Tag")
    status = models.BooleanField(default=True, verbose_name="Status")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Yaranma tarixi")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Yenilənmə tarixi")

    def __str__(self):
        return self.name