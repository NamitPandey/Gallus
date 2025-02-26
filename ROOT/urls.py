#this is urls file of the project


from django.urls import path
from . import views as views
from django.contrib.auth import views as auth_views

app_name="gallus"

urlpatterns = [
    path("",views.site_index, name="site_index"),
    # path("login",appview.login_index, name="login"),
    path('login', auth_views.LoginView.as_view(),name='login'),
    path('logout', auth_views.LogoutView.as_view(),name="logout"),
    
    
]