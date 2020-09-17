from django.contrib import admin
from .models import *

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'userType')

admin.site.register(User, UsersAdmin)
