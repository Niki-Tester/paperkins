from django.urls import path
from . import views

urlpatterns = [
    path('request', views.contact_request, name='contact_request'),
]
