from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render
from .models import *
# Create your views here.

def site_index(request):

    about_us = ViewManager.objects.filter(banner_type="About_Us")
    welcome_text = ViewManager.objects.filter(banner_type="Welcome_Screen").order_by("added_on")
    print(welcome_text)
    context = {
        "welcome_text":welcome_text,
        "about_us":about_us,
    }

    return render(request, "Site_Home/index.html",context=context)


