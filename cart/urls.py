from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_cart, name="view_cart"),
    path("add/<item_id>", views.add_to_cart, name="add_to_cart"),
    path("update/<item_id>", views.update_cart_item, name="update_cart_item"),
    path("remove/<item_id>", views.remove_cart_item, name="remove_cart_item"),
]
