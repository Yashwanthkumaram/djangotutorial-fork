from django.urls import path

from . import views

urlpatterns = [
    # path("", views.respond, name="respond"),
    # path("", views.index, name="index"),
    path("", views.get_name, name="get_name"),

    # path("<element_id>/", views.resp, name="resp"),

]