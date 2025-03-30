from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render
from .models import *
# Create your views here.

def site_index(request):

    about_us = ViewManager.objects.filter(banner_type="About_Us")
    welcome_text = ViewManager.objects.filter(banner_type="Welcome_Screen").order_by("added_on")
    feedback_text = ViewManager.objects.filter(banner_type="Feedback").order_by("added_on")
    our_products = Products_List.objects.all().distinct()
    print(list(feedback_text))
    context = {
        "welcome_text":welcome_text,
        "about_us":about_us,
        "our_products":our_products,
        "feedback_text":feedback_text,
    }

    return render(request, "Site_Home/index.html",context=context)


