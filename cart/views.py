from django.shortcuts import render, redirect


def view_cart(request):
    """ A view to render the shopping cart page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add product to shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    custom_message = None
    if 'custom_message' in request.POST:
        custom_message = request.POST.get('custom_message')
    cart = request.session.get('cart', {})

    if custom_message or custom_message == '':
        if item_id in list(cart.keys()):
            if custom_message in cart[item_id]['items_by_message'].keys():
                cart[item_id]['items_by_message'][custom_message] += quantity
            else:
                cart[item_id]['items_by_message'][custom_message] = quantity
        else:
            cart[item_id] = {'items_by_message': {custom_message: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
