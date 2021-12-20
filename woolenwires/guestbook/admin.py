from django.contrib import admin

# Register your models here.

from .models import Guest, GuestBookEntry
 
@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Guest._meta.get_fields()]
    pass

@admin.register(GuestBookEntry)
class GuestBookAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GuestBookEntry._meta.get_fields()]
