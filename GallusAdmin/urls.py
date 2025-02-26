from django.urls import path
from . import views

app_name="Gallus_Admin"

urlpatterns = [
    path("", views.GallusAdmin, name="GallusAdmin"),
    path("UnauthorizedAccess", views.UnauthorizedAccess, name="UnauthorizedAccess")
]

