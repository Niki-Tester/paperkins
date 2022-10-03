from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_content(request):

    cart_items = []
    total = 0
    product_count = 0
    subtotal = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        product = Product.objects.filter(pk=item_id)
        if not product:
            cart.pop(item_id)
            break
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            subtotal = product.price * item_data
            total += product.price * item_data
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'subtotal': subtotal,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            item_data_by_message = item_data['items_by_message'].items()
            for custom_message, quantity in item_data_by_message:
                subtotal = product.price * quantity
                total += quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'custom_message': custom_message,
                    'subtotal': subtotal,
                })

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    grand_total = total + delivery

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
        'cart': cart
    }

    return context
