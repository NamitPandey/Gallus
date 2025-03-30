from ROOT import views
from ROOT.models import *
from django.urls import reverse, reverse_lazy
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
    
class ManageSite(FormView):
    model = WelcomeForm
    form_class = WelcomeForm
    second_form_class = FeedbackForm
    template_name = "Gallus_Admin/manage_site.html"

    def get_context_data(self, **kwargs):
        context = super(ManageSite, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()

        context["all_welcome_data"] = ViewManager.objects.filter(banner_type="Welcome_Screen")
        context["all_feedback_data"] = ViewManager.objects.filter(banner_type="Feedback")
        context["aboutUs"] = ViewManager.objects.filter(banner_type="About_Us")
        return context


    def form_valid(self, form):
        if form.is_valid():
            obj = form.save(commit=False)
            obj.added_by = self.request.user.username
            obj.save()
        return super().form_valid(form)
    
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

def submitForm(request, formNumber):
    form_type={
        1:"WelcomeForm(request.POST)",
        2:"FeedbackForm(request.POST)"
    }
    try:
        if request.method == "POST":
            form = eval(form_type[formNumber])
            if form.is_valid:
                obj = form.save(commit=False)
                obj.added_by = request.user.username
                obj.save()

            return HttpResponseRedirect(reverse_lazy("Gallus_Admin:manage_site"))
    except Exception as e:
        print(e)

def deleteSiteContent(request,pk):
    try:
        obj_data = ViewManager.objects.get(id=pk)
        obj_data.delete()
        return HttpResponseRedirect(reverse_lazy("Gallus_Admin:manage_site"))

    except Exception as e:
        print(e)

def updateSiteContent(request,pk):
    form_select = {
                "Welcome_Screen": "WelcomeForm",
                "About_Us": "AboutUsForm",
                "Feedback": "FeedbackForm"
            }
    try:
        if request.method != "POST":
            context = {"pk":pk}            
            form_type = list(ViewManager.objects.filter(id=pk).values("banner_type"))[0]["banner_type"]
            form_name = form_select[f"{form_type}"]
            fields = eval(f"{form_name}").Meta.fields
            query_string =f"ViewManager.objects.filter(id=pk).values("
            for index, name in enumerate(fields):
                query_string+=f"'{name}',"
                if index+1 == len(fields):
                    query_string+=")"
            query_res = eval(query_string)
            choiceVal = list(query_res)[0]
            if form_name == "FeedbackForm":
                context["title"] = form_type.replace("_"," ")
            else:
                context["title"] = form_type.replace("_"," ")
            context["form"] = eval(f"{form_name}")(choiceVal= choiceVal)
            return render(request, "Gallus_Admin/edit_site_content.html", context=context)
    
        if request.method == "POST":
            post_form = list(ViewManager.objects.filter(id=pk).values("banner_type"))[0]["banner_type"]
            print(post_form)
            form_name = form_select[post_form]
            query_string = f"{form_name}(data=request.POST)"
            form = eval(query_string)
            if form.is_valid():
                viewObj = ViewManager.objects.get(id=pk)
                if request.POST.get("banner_type") == "Feedback":
                    viewObj.feedback_by = request.POST.get("feedback_by")
                    viewObj.client_company = request.POST.get("client_company")
                    viewObj.banner_title = "not_available"
                else:
                    viewObj.banner_title = request.POST.get("banner_title")
                viewObj.title_text = request.POST.get('title_text')
                viewObj.updated_by = request.user.username
                viewObj.save()

        return HttpResponseRedirect(reverse_lazy("Gallus_Admin:manage_site"))

    except Exception as e:
        print(e)

