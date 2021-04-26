from django.urls import path

from .views import index, add_product

urlpatterns = [
    path("", index, name="index"),
    path("add/", add_product, name="add"),
]
