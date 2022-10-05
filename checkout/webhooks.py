from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import StripeWH_Handler
import stripe


@require_POST
@csrf_exempt
def webhook(request):
    """ Listen for webhooks from Stripe """
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    wh_secret = settings.STRIPE_WEBHOOK_KEY
    stripe.api_key = settings.STRIPE_CLIENT_SECRET
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret)

    except ValueError as e:
        # Invalid Payload
        return HttpResponse(content=e, status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid Signature
        return HttpResponse(content=e, status=400)
    except Exception as e:
        # Unhandled Exception
        return HttpResponse(content=e, status=400)

    # Handle the events
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handset functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed':
        handler.handle_payment_intent_payment_failed,
    }

    # Get the webhook type from Stripe
    event_type = event['type']
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return response
