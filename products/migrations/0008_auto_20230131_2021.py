# Generated by Django 3.2.16 on 2023-01-31 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_product_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('default', models.BooleanField(default=False)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.imagealbum')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='album',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model', to='products.imagealbum'),
        ),
    ]
