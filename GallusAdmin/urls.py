from django.urls import path
from GallusAdmin import views

app_name="Gallus_Admin"

urlpatterns = [
    path("", views.GallusAdmin, name="GallusAdmin"),
    path("UnauthorizedAccess", views.UnauthorizedAccess, name="UnauthorizedAccess"),
    path("addProduct", views.CreateProducts.as_view(), name="addProduct"),
    path("deleteProduct/<int:id>", views.DeleteProduct.as_view(), name="deleteProduct")

]

