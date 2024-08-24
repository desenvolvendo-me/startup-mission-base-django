from django.shortcuts import redirect
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import stripe
import json

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        try:
            lookup_key = request.POST.get('lookup_key')
            prices = stripe.Price.list(
                lookup_keys=[lookup_key],
                expand=['data.product']
            )

            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': prices.data[0].id,
                        'quantity': 1,
                    },
                ],
                mode='subscription',
                success_url=settings.YOUR_DOMAIN + '/payments/success/',
                cancel_url=settings.YOUR_DOMAIN + '/payments/cancel/',
            )

            return JsonResponse({'checkout.html': checkout_session.url})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class CustomerPortalView(View):
    def post(self, request, *args, **kwargs):
        checkout_session_id = request.POST.get('session_id')
        checkout_session = stripe.checkout.Session.retrieve(checkout_session_id)

        portal_session = stripe.billing_portal.Session.create(
            customer=checkout_session.customer,
            return_url=settings.YOUR_DOMAIN + '/account/',
        )

        return redirect(portal_session.url)


@method_decorator(csrf_exempt, name='dispatch')
class StripeWebhookView(View):
    def post(self, request, *args, **kwargs):
        webhook_secret = 'whsec_12345'
        payload = request.body
        sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
        event = None

        try:

            event = stripe.Webhook.construct_event(
                payload, sig_header, webhook_secret
            )
        except ValueError as e:

            return JsonResponse({'error': 'Invalid payload'}, status=400)
        except stripe.error.SignatureVerificationError as e:

            return JsonResponse({'error': 'Invalid signature'}, status=400)

        if event['type'] == 'checkout.session.completed':
            print('🔔 Payment succeeded!')
        elif event['type'] == 'customer.subscription.created':
            print('🔔 Subscription created!')
        elif event['type'] == 'customer.subscription.updated':
            print('🔔 Subscription updated!')
        elif event['type'] == 'customer.subscription.deleted':
            print('🔔 Subscription canceled!')
        elif event['type'] == 'customer.subscription.trial_will_end':
            print('🔔 Subscription trial will end!')

        return JsonResponse({'status': 'success'})


class SuccessView(TemplateView):
    template_name = 'payments/success.html'


class CancelView(TemplateView):
    template_name = 'payments/cancel.html'
