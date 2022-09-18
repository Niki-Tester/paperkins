from decimal import Decimal
from django.conf import settings


def cart_content(request):

    cart_items = []
    total = 0
    product_count = 0

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)

    grand_total = total + delivery

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total
    }

    return context
