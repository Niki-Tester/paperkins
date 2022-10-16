from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.template.loader import render_to_string

from .forms import ContactForm, ResponseForm
from .models import Contact


@login_required
def customer_queries(request):
    """ Display a list of customer queries to the user """
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to view this page')
        return redirect(reverse('home'))

    form = ResponseForm()
    queries = Contact.objects.all()
    context = {
        'form': form,
        'queries': queries
    }

    return render(request, 'contact/customer_queries.html', context)


@login_required
@require_POST
def send_response(request, id):
    """ Send an email response to customer """
    response = ResponseForm(request.POST)
    if response.is_valid():
        query = Contact.objects.get(id=id)
        query.response_message = response.cleaned_data['response_message']
        query.response_sent = True
        query.save()
        subject = render_to_string(
            'contact/response_emails/response_email_subject.txt', {
                'request': request,
                'query': query,
            })

        message = render_to_string(
            'contact/response_emails/response_email_body.txt', {
                'request': request,
                'contact_email': settings.DEFAULT_FROM_EMAIL,
                'query': query,
            })

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,
                  [query.contact_email])
        messages.success(
            request, f'Response sent successfully to {query.contact_email}')
    return redirect(reverse('customer_queries'))


@login_required
@require_POST
def contact_request(request):
    """ Process contact form sent from user """
    contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
        query = contact_form.save()
        subject = render_to_string(
            'contact/confirmation_emails/new_contact_email_subject.txt', {
                'request': request,
                'query': query,
            })

        message = render_to_string(
            'contact/confirmation_emails/new_contact_email_body.txt', {
                'request': request,
                'query': query,
                'contact_email': settings.DEFAULT_FROM_EMAIL,
            })

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,
                  [contact_form.cleaned_data['contact_email']])
        messages.success(request, 'Your message was successfully sent')
    else:
        messages.error(request, 'There was an error sending your message, '
                       f'Error: {contact_form.errors.as_text()}')
        contact_form.delete()

    return redirect(request.META['HTTP_REFERER'])


@login_required
def remove_query(request, id):
    """ Remove a customers query """
    if not request.user.is_superuser:
        messages.error(
            request, 'You are not authorized to perform this action')
        return redirect(reverse('home'))

    try:
        query = Contact.objects.get(id=id)
        query.delete()

        messages.success(request, 'Query successfully removed')

    except Contact.DoesNotExist as e:
        messages.error(request, f'Error removing query. ERROR: {e}')

    return redirect(reverse('customer_queries'))
