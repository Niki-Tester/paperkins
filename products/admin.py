from django.contrib import admin
from .models import Product, Category, Image


@admin.action(description="Mark selected as active")
def make_active(modeladmin, request, queryset):
    queryset.update(active=True)


@admin.action(description="Mark selected as inactive")
def make_inactive(modeladmin, request, queryset):
    queryset.update(active=False)


class Images(admin.TabularInline):
    model = Image
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "stock_qty", "active")
    ordering = ("name",)
    actions = [make_active, make_inactive]
    inlines = [
        Images,
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


class ImageAdmin(admin.ModelAdmin):
    list_display = ("file_name", "product")


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)
