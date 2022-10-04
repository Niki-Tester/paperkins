from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
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

    current_cart = cart_content(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_client_secret
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key not found!')

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
