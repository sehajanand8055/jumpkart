# Generated by Django 2.0.3 on 2018-07-14 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jumpkart', '0004_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
