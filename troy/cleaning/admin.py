from django.contrib import admin
from .models import contact_to_hire , appointment , Record_mail_me

# Register your models here.

@admin.register(contact_to_hire)
class contact_to_hireAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'message', 'company', 'date', 'seen')  # Add 'seen' to the list_display
    list_filter = ('name', 'email', 'phone', 'subject', 'message', 'company', 'date')
    ordering = ('name',)
    search_fields = ('name', 'email', 'phone', 'subject', 'message', 'company', 'date')
    list_editable = ('seen',)  # Add 'seen' to the list_editable fields

    def get_list_display(self, request):
        """
        Customize the list_display based on user permissions.
        For example, only superusers can see the 'seen' field.
        """
        if request.user.is_superuser:
            return self.list_display
        else:
            return tuple(field for field in self.list_display if field != 'seen')

    def has_change_permission(self, request, obj=None):
        """
        Only allow superusers to change the 'seen' field.
        """
        if obj is not None and not request.user.is_superuser:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        """
        Only allow superusers to delete items.
        """
        if obj is not None and not request.user.is_superuser:
            return False
        return True
    
@admin.register(appointment)

class appointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'appointment_date', 'adress', 'date', 'seen')
    list_filter = ('name', 'email', 'phone', 'appointment_date', 'adress', 'date')
    ordering = ('name',)
    search_fields = ('name', 'email', 'phone', 'appointment_date', 'adress', 'date')
    list_editable = ('seen',)  # Add 'seen' to the list_editable fields

    def get_list_display(self, request):
        """
        Customize the list_display based on user permissions.
        For example, only superusers can see the 'seen' field.
        """
        if request.user.is_superuser:
            return self.list_display
        else:
            return tuple(field for field in self.list_display if field != 'seen')
        
    def has_change_permission(self, request, obj=None):
        """
        Only allow superusers to change the 'seen' field.
        """
        if obj is not None and not request.user.is_superuser:
            return False
        return True
    
    def has_delete_permission(self, request, obj=None):
        """
        Only allow superusers to delete items.
        """
        if obj is not None and not request.user.is_superuser:
            return False
        return True
    
@admin.register(Record_mail_me)
class Record_mail_meAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'topic', 'created_at')
    list_filter = ('name', 'email', 'phone', 'topic', 'created_at')
    ordering = ('name',)
    search_fields = ('name', 'email', 'phone', 'topic', 'created_at')
    
    def has_change_permission(self, request, obj=None):
        """
        Only allow superusers to change the 'seen' field.
        """
        if obj is not None and not request.user.is_superuser:
            return False
        return True
    
    def has_delete_permission(self, request, obj=None):
        """
        Only allow superusers to delete items.
        """
        if obj is not None and not request.user.is_superuser:
            return False
        return True

