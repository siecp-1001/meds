from django.contrib import admin

from . import models
from django.contrib.auth.admin import (
    UserAdmin as DjangoUserAdmin
)

# Register your models here.


@admin.register(models.user)

class useradmin (DjangoUserAdmin):
    fieldsets=(
        (None,{"fields":("email","password")}),
        (
            "personal info",
            {"fields":("first_name","last_name")},
        ),
        (
            "permissions",
            {
                "fields":(
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    
                )
            },
        ),
        (
            "important dates",
            {"fields":("last_login","date_joined")},
        ),
        
    )
    add_fieldsets=(
        (
            None,
            {
                "classes":("wide",),
                "fields":("email","password1","password2"),
            },
        ),
    )
    list_display=(
        "email",
        "first_name",
        "last_name",
        "is_staff"
    )
    search_fields=("email","first_name","last_name")
    ordering=("email",)