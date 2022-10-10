from .forms import ContactForm


def contact_us_form(request):
    """ Add newsletter form to context api """
    contact_form = ContactForm()
    context = {
        'contact_form': contact_form,
    }

    return context
