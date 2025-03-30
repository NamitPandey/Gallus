from django.urls import path
from GallusAdmin import views
from gallus import settings
from django.contrib.auth.decorators import login_required

app_name="Gallus_Admin"


urlpatterns = [
    path("", views.GallusAdmin, name="GallusAdmin"),
    path("UnauthorizedAccess", views.UnauthorizedAccess, name="UnauthorizedAccess"),
    path("addProduct", login_required(views.CreateProducts.as_view(), login_url=settings.LOGIN_URL), name="addProduct"),
    path("updateProduct/<int:pk>/", login_required(views.UpdateProduct.as_view(),login_url=settings.LOGIN_URL), name="updateProduct"),
    path("deleteProduct/<int:pk>", login_required(views.DeleteProduct.as_view(), login_url=settings.LOGIN_URL), name="deleteProduct"),
    path("manage_site", login_required(views.ManageSite.as_view(), login_url=settings.LOGIN_URL), name="manage_site"),
    path("submitForm/<int:formNumber>", views.submitForm, name="submitForm"),
    path("updateSiteContent/<int:pk>", views.updateSiteContent, name="updateSiteContent"),
    path("deleteSiteContent/<int:pk>", views.deleteSiteContent, name="deleteSiteContent")
]

