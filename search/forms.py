from django import forms
from django.core.mail import send_mail
from django.contrib.auth.forms import(
    UserCreationForm as Djangousercreationform
)
from django.contrib.auth.forms import UsernameField
from . import models
from django.contrib.auth import authenticate
from django.forms import inlineformset_factory

import logging





class Usercreationform(Djangousercreationform):
    class Meta(Djangousercreationform.Meta):
        model=models.user
        fields=("email",)
        field_class={"email":UsernameField}
    def send_mail(self):
        logging.Logger.info(
            "sending signup email for email =%s",
            self.cleaned_data["email"],
        )
        message="welcome{}".format(self.cleaned_data["email"])
        send_mail(
            "welcome to Booktime",
            message,
            "site@booktime.domain",
            [self.cleaned_data["email"]],
            fail_silently=True,
        )        
        
        
class authenticationform(forms.Form):
    email=forms.EmailField()
    passsword= forms.CharField(
        strip=False,widget=forms.PasswordInput
    )  
    def __init__(self,request=None,*args,**kwargs):
        self.request=request
        self.user=None
        super().__init__(*args,**kwargs)
    def clean(self) :
        email=self.cleaned_data.get("email")
        password=self.cleaned_data.get("password")
        if email is not None and password:
            self.user=authenticate(
                self.request,email=email ,password=password
            )
            if self.user is None:
                raise forms.ValidationError(
                    "invalid email/password combination."
                )
            logging.Logger.info(
                "authincation is valiad for email=%s",email
            )    
        return self.cleaned_data
    def get_user(self):
        return self.user      





