from django.urls import path
from .  import views
from django.views.generic import TemplateView
from . import views,models
from django.views.generic.detail import DetailView
from django.contrib.auth import views as auth_views
from . import forms
app_name='search'
urlpatterns=[
     path("login/",auth_views.LoginView.as_view(template_name="login.html",form_class=forms.authenticationform,),name="login",),
    path("signup/", views.signupview.as_view(), name="signup"),
]
