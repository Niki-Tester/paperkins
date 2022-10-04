from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from products.models import Product
from .models import OrderLineItem, Order
from .forms import OrderForm
from cart.contexts import cart_content

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_client_secret = settings.STRIPE_CLIENT_SECRET
    cart = request.session.get('cart', {})

    if not cart:
        messages.error(
            request, 'There is noting in you shopping cart at the moment')
        return redirect(reverse('products'))

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address_1': request.POST['street_address_1'],
            'street_address_2': request.POST['street_address_2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(pk=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order-order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        items = item_data['items_by_message'].items()
                        for custom_message, quantity in items:
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                custom_message=custom_message
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        'One or more of the items in your cart was not '
                        'found in our database. '
                        'Please contact us for assistance!'
                    ))
                    order.delete()
                    return redirect(reverse('view_cart'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form'
                           'Please double check your information.')

    else:
        current_cart = cart_content(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_client_secret
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key not found!')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save-info')  # noqa
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, 'Order successfully processed! '
                     f'Your order number is {order_number}. A confirmation '
                     f'email will be sent to f{order.email}')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order
    }

    return render(request, template, context)
