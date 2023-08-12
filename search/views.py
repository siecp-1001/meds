from os import path
from django.core.mail import send_mail
from django.shortcuts import render, redirect,get_object_or_404
from django.template.loader import render_to_string
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from main import forms
from django.views.generic.list import ListView
from .forms import  ContactForm
from main import forms,models
from django.shortcuts import get_object_or_404, render
from.models import basketline, product, producttag, Room, Message
import logging
from django.contrib.auth import login ,authenticate
from django.contrib import messages
# offer users a way to add, change, and remove their addresses
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django .views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django .views.generic.edit import (
     FormView,
     CreateView,
     UpdateView,
     DeleteView,
    )
from . import models
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse

# Create your views here.


logger= logging.getLogger(__name__)

class signupview(FormView):
    template_name="signup.html"
    form_class=forms.Usercreationform
    def get_success_url(self) :
        redirect_to=self.request.GET.get("next","/")
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
        form.send_mail()
        messages.info(
            self.request,"you signed up succesfully"
        )
        return response