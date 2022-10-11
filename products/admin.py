from django.contrib import admin
from .models import Product, Category


@admin.action(description='Mark selected as active')
def make_active(modeladmin, request, queryset):
    queryset.update(active=True)


@admin.action(description='Mark selected as inactive')
def make_inactive(modeladmin, request, queryset):
    queryset.update(active=False)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'stock_qty', 'active')
    ordering = ('name',)
    actions = [make_active, make_inactive]


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
