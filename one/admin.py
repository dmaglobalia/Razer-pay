from django.contrib import admin

# Register your models here.
from .models import pay

@admin.register(pay)
class x(admin.ModelAdmin):
    list_display = ['id','payment']