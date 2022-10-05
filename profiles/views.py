from django.shortcuts import render


def profile(request):
    """ A view for rendering user profiles """
    context = {}
    return render(request, 'profiles/profile.html', context)
