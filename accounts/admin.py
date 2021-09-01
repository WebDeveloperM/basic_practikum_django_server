from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.

class CustonUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name', 'email', 'adress', 'age', 'is_staff']


    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('age',) }),
    )

    add_fieldsets =UserAdmin.add_fieldsets+(
        (None, {'fields': ('age',)}),
    )



admin.site.register(CustomUser, CustonUserAdmin)

