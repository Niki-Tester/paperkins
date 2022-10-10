from .forms import NewsletterForm


def newsletter_footer_form(request):
    """ Add newsletter form to context api """
    newsletter_form = NewsletterForm()
    context = {
        'newsletter_form': newsletter_form,
    }

    return context
