# Generated by Django 3.1.6 on 2021-02-11 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210208_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantity',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.size'),
        ),
        migrations.AlterUniqueTogether(
            name='quantity',
            unique_together={('product_item', 'size')},
        ),
    ]
