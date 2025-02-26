from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(ViewManager)
admin.site.register(Products_List)
admin.site.register(UnauthorizedAccess_Tracker)