from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ A view for rendering user profiles """
    profile = get_object_or_404(UserProfile, user=request.user)
    print(profile.__dict__)

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
