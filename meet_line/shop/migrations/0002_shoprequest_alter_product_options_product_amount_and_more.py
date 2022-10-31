# Generated by Django 4.1 on 2022-10-31 01:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import shop.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=40, verbose_name='Идентификатор корзины')),
                ('name', models.CharField(help_text='Введите имя по которому к вам можно обращатся', max_length=30, verbose_name='Имя покупателя')),
                ('phone', models.CharField(help_text='Введите номер вашего мобильного телефона', max_length=20, validators=[django.core.validators.RegexValidator(message='Введите номер мобильного телефона', regex='(\\+7|8)[- _]*\\(?[- _]*(\\d{3}[- _]*\\)?([- _]*\\d){7}|\\d\\d[- _]*\\d\\d[- _]*\\)?([- _]*\\d){6})')], verbose_name='Номер телефона для связи')),
                ('address', models.CharField(help_text='Введите адрес по которому доставить покупки', max_length=300, verbose_name='Адрес доставки')),
                ('comment', models.TextField(blank=True, help_text='Введите комментарий (если необходим)', max_length=300, null=True, verbose_name='Комментарий')),
                ('is_delivered', models.BooleanField(default=False, verbose_name='Доставка выполнена?')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.CharField(choices=[('kg', 'кг'), ('pcs', 'шт')], default='kg', max_length=3, verbose_name='Мера (кг или шт)'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='Товар доступен?'),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture_url',
            field=models.ImageField(upload_to='images/', verbose_name='Фото товара'),
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=1, max_digits=3, null=True, validators=[shop.validators.validate_card_quantity], verbose_name='Колличество')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена')),
                ('card_id', models.CharField(max_length=40, verbose_name='Идентификатор корзины')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Товар')),
            ],
        ),
        migrations.AddConstraint(
            model_name='card',
            constraint=models.UniqueConstraint(fields=('product', 'card_id'), name='unique_card_product', violation_error_message='Card can only have one instance of a product'),
        ),
    ]
