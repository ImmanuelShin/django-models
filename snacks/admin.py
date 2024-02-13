from django.contrib import admin
from .models import Snack

# Register your models here.

class SnackAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'reviewer', 'description')

admin.site.register(Snack)