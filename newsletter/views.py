from django.shortcuts import redirect, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from .forms import NewsletterForm
from .models import Newsletter


@require_POST
def subscribe(request):
    """Allows users to signup to the newsletter"""
    newsletter_form = NewsletterForm(request.POST)

    if newsletter_form.is_valid():
        newsletter_form.save()
        subscriber = Newsletter.objects.get(
            newsletter_email=newsletter_form.cleaned_data["newsletter_email"]
        )

        subject = render_to_string(
            "newsletter/confirmation_emails/confirmation_email_subject.txt",
            {
                "request": request,
            },
        )

        message = render_to_string(
            "newsletter/confirmation_emails/confirmation_email_body.txt",
            {
                "request": request,
                "name": newsletter_form.cleaned_data["newsletter_name"],
                "contact_email": settings.DEFAULT_FROM_EMAIL,
                "unsubscribe_url": request.build_absolute_uri("unsubscribe"),
                "subscriber_uid": subscriber.uid,
            },
        )

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [newsletter_form.cleaned_data["newsletter_email"]],
        )

        messages.success(
            request,
            "Thank you for signing up to our newsletter."
            " A confirmation email has been sent to "
            f'{newsletter_form.cleaned_data["newsletter_email"]}',
        )
    else:
        messages.error(
            request,
            "Error signing up to newsletter."
            f"{newsletter_form.errors.as_text()}",
        )

    return redirect(request.META["HTTP_REFERER"])


def unsubscribe(request, uid):
    """Allow user to opt out of newsletter after signup"""
    try:
        subscriber = Newsletter.objects.get(uid=uid)

        subscriber.delete()
    except Newsletter.DoesNotExist:
        return HttpResponse(
            "You have already unsubscribed " "from our newsletter"
        )

    return HttpResponse("You have been unsubscribed from our newsletter")
