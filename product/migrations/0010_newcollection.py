# Generated by Django 5.1.7 on 2025-04-15 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_salesproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewCollection',
            fields=[
            ],
            options={
                'verbose_name': 'NewCollection',
                'verbose_name_plural': 'NewCollection',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('product.product',),
        ),
    ]
