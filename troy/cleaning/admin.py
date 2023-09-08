from django.contrib import admin
from .models import contact_to_hire

# Register your models here.

@admin.register(contact_to_hire)
class contact_to_hireAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone','subject','message','company','date')
    list_filter = ('name', 'email', 'phone','subject','message','company','date')
    ordering = ('name',)
    search_fields = ('name', 'email', 'phone','subject','message','company','date')
    
