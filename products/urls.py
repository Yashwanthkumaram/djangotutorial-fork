from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products", views.products, name="products"),
    path("products/<cat_name>", views.product, name="product"),
]