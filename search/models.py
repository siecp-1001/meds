from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
)
from datetime import datetime
from django.core.validators import MinValueValidator

# Create your models here.

class Activemanager(models.Manager):
    def active(self):
        return self.filter(active=True) 
    


class usermanager(BaseUserManager):
    use_in_migrations=True
    def _create_user(self,email,password,**extra_fields):
        if not email :
            raise ValueError("the given email must be set")
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
    def create_user(self,email,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser",False)
        return self._create_user(email,password,**extra_fields)
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "superuser must have is_staff=True."
            )    
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "superuser must have is_superuser=True."
            )   
        return self._create_user(email,password,**extra_fields)



class user(AbstractUser) :
    username=None
    email=models.EmailField('email address',unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=usermanager()   
         