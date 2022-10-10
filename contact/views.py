from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from django.conf import settings
from django.template.loader import render_to_string

from .forms import ContactForm


@require_POST
def contact_request(request):
    """ Process contact form sent from user """
    form_data = request.POST
    contact_form = ContactForm(form_data)
    if contact_form.is_valid():
        contact_form.save()
        subject = render_to_string(
            'contact/confirmation_emails/new_contact_email_subject.txt', {
                'request': request,
            })

        message = render_to_string(
            'contact/confirmation_emails/new_contact_email_body.txt', {
                'request': request,
                'users_name': contact_form.cleaned_data['name'],
                'users_email': contact_form.cleaned_data['email'],
                'users_query': contact_form.cleaned_data['query'],
                'users_message': contact_form.cleaned_data['message'],
                'contact_email': settings.DEFAULT_FROM_EMAIL,
            })

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,
                  [contact_form.cleaned_data['email']])
        messages.success(request, 'Your message was successfully sent')
    else:
        messages.error(request, 'There was an error sending your message, '
                       f'Error: {contact_form.errors.as_text()}')
        contact_form.delete()

    return redirect(request.META['HTTP_REFERER'])
