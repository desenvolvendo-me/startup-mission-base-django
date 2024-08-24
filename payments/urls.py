from django.urls import path
from .views import CreateCheckoutSessionView, CustomerPortalView, StripeWebhookView, SuccessView, CancelView

urlpatterns = [
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('create-portal-session/', CustomerPortalView.as_view(), name='customer-portal'),
    path('webhook/', StripeWebhookView.as_view(), name='webhook'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
]
