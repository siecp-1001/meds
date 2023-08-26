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
    path( "products/", views.productlistview.as_view(), name="products" ),
    path("products/<slug:tag>/", views.productlistview.as_view(),name="products",),
    path("product/<slug:slug>/", DetailView.as_view(model= models.product),name="product",),   
    path("",TemplateView.as_view(template_name="pages/home.html"),name="home",),
    path('create-pdf', views.pdf_report_create, name='create-pdf'),
]
