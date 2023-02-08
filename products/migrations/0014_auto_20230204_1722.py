# Generated by Django 3.2.16 on 2023-02-04 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20230204_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='products.product'),
        ),
    ]