from ROOT import views
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from ROOT.models import UnauthorizedAccess_Tracker, Products_List
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, FormView, DeleteView, UpdateView

from .forms import *

# CBV views

class CreateProducts(FormView):
    model = Products_List
    form_class = ProjectForm
    template_name = "Gallus_Admin/product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Add Product"
        context['product_types'] = [prod_type[0] for prod_type in Products_List.CHOICES]
        return context
    
    def form_valid(self, form):
        if form.is_valid():
            obj = form.save(commit=False)
            obj.added_by = self.request.user.username
            obj.save()
        return super().form_valid(form)
    
    def get_success_url(self):

        return reverse("Gallus_Admin:GallusAdmin")
    
# update view

class UpdateProduct(UpdateView):
    model=Products_List
    fields=[
        "product_type",
        "product_name",
        "product_description",
        "price",
    ]
    template_name = "Gallus_Admin/modifyProduct.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Update Product"
        context["product_types"] = [prod_type[0] for prod_type in Products_List.CHOICES]
        return context
    
    def form_valid(self, form):
        if form.is_valid():
            obj = form.save(commit=False)
            obj.updated_by = self.request.user.username
            obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("Gallus_Admin:GallusAdmin")
    
# delete view 
class DeleteProduct(DeleteView):
    models = Products_List
    template_name = "Gallus_Admin/modifyProduct.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Delete Product"
        return context
    
    def get_object(self):
        id = self.kwargs.get("pk")
        return get_object_or_404(Products_List, id=id)
    
    def get_success_url(self):
        return reverse("Gallus_Admin:GallusAdmin")
    


# CBV views end




# Create your views here.

@login_required(login_url='/GallusAdmin/UnauthorizedAccess')
def GallusAdmin(request):
    context={}
    try:
        products_list = Products_List.objects.all()    
        total_products = len(products_list)    
        logged_in_users = len(get_all_logged_in_users())

        context.update({
            "logged_in_users":logged_in_users,
            "products_list":products_list,
            "total_products":total_products
            })

        return render(request, "Gallus_Admin/index.html", context=context)
    except Exception as e:
        print(e)
        return HttpResponseRedirect(views.site_index)


def UnauthorizedAccess(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = "None"
    if x_forwarded_for:
        ip = str(x_forwarded_for.split(',')[0])
    else:
        ip = str(request.META.get('REMOTE_ADDR'))

    save_tracker = UnauthorizedAccess_Tracker.objects.create(track_log=f"{request.META}",ip_logged=ip)
    save_tracker.save()

    return render(request, "Unauthorized_Access/403.html", context={})

def get_all_logged_in_users():
    # Query all non-expired sessions
    # use timezone.now() instead of datetime.now() in latest versions of Django
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []

    # Build a list of user ids from that query
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))

    # Query all logged in users based on id list
    return User.objects.filter(id__in=uid_list)

