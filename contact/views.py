from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import ContactForm


@require_POST
def contact_request(request):
    form_data = request.POST
    contact_form = ContactForm(form_data)
    if contact_form.is_valid():
        messages.success(request, 'Your message was successfully sent')
        contact_form.save()
    else:
        messages.error(request, 'There was an error sending your message, '
                       f'Error: {contact_form.errors.as_text()}')
        contact_form.delete()

    return redirect(request.META['HTTP_REFERER'])
