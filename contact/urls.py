from django.urls import path
from . import views

urlpatterns = [
    path("", views.customer_queries, name="customer_queries"),
    path("request/", views.contact_request, name="contact_request"),
    path("send_response/<id>", views.send_response, name="send_response"),
    path("remove_query/<id>", views.remove_query, name="remove_query"),
]
