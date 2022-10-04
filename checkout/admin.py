from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInLine(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInLine,)
    readonly_fields = (
        'order_number',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_cart',
        'stripe_pid',
    )

    fields = (
        'order_number',
        'date',
        'full_name',
        'email',
        'phone_number',
        'street_address_1',
        'street_address_2',
        'town_or_city',
        'country',
        'postcode',
        'county',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_cart',
        'stripe_pid',
    )

    list_display = (
        'order_number',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
