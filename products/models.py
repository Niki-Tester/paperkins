from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_init, post_save


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Catagories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.friendly_name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock_qty = models.IntegerField(default=0)
    has_custom_message = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    file_name = models.ImageField(null=True, blank=True)
    default = models.BooleanField(default=False)
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name="images",
    )

    def __str__(self):
        return self.file_name.name
