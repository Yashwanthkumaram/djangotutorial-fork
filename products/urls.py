from django.urls import path

from . import views

urlpatterns = [
    # path("", views.respond, name="respond"),
    path("", views.index, name="index"),

    path("<element_id>/", views.resp, name="resp"),

]