from django.http import HttpResponse
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
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
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
    



class productlistview(ListView):
    template_name="pages/product_list.html"
    model = models.product
    paginate_by=7
    context_object_name="products"
    def  get_queryset(self):
      return models.product.objects.all()[:7]  
    




def pdf_report_create(request):
    products = models.product.objects.all()

    template_path = 'pdfReport.html'

    context = {'products': products}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="products_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response