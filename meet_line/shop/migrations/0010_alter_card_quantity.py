# Generated by Django 4.1 on 2022-10-04 00:15

from django.db import migrations, models
import shop.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_card_unique_card_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True, validators=[shop.validators.validate_card_quantity], verbose_name='Колличество'),
        ),
    ]