from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm


def profile(request):
    """ A view for rendering user profiles """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'You default delivery information '
                             'has been updated')
        else:
            form.delete()
            messages.error(request, 'Error saving delivery information, '
                           'please check your details and try again')
            return redirect(reverse('profile'))

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    context = {
        'orders': orders,
        'form': form,
        'profile': profile
    }
    return render(request, 'profiles/profile.html', context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request,
                  'This is a past confirmation for '
                  f'order number: {order.order_number}. '
                  f'A confirmation email was sent to: {order.email} '
                  f'on {order.date}')
    template = 'checkout/checkout_success.html'
    context = {
        'order': order
    }

    return render(request, template, context)
