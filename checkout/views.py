from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(
            request, 'There is noting in you shopping cart at the moment')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LGkzyCe6AWfkdOa6zwd6F9FygoxC9XLA0gMp6zV4tv9PPRFBdulDaAKvHtx1fKlZ1NwbzfjWFZo1E3OROCUyWLI004Gr21DGO',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
