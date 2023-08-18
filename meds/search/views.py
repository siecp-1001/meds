from django.shortcuts import render
from django.views.generic.edit import FormView

from . import models
from . import forms
import logging
from django.contrib.auth import login ,authenticate
from django.contrib import messages
# offer users a way to add, change, and remove their addresses
from django .views.generic.edit import FormView
from django .views.generic.edit import (
     FormView,
    )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
# Create your views here.

def home(request):
    return render(request, "home.html", {})
logger= logging.getLogger(__name__)

class signupview(FormView):
    template_name="signup.html"
    form_class=forms.Usercreationform
    def get_success_url(self) :
        redirect_to=self.request.GET.get("next","")
        return redirect_to
    def form_valid(self, form) :
        response=super().form_valid(form)
        form.save()
        email=form.cleaned_data.get("email")
        raw_password=form.cleaned_data.get("password1")
        logger.info(
            "new signup for email =%s through signupview",email
        )
        user=authenticate(email=email,password=raw_password)
        login(self.request,user)
       
        return response
    



class notelistview(LoginRequiredMixin,ListView):
    model=models.product
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)    