from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'query', 'date_time')
    ordering = ('-date_time',)


admin.site.register(Contact, ContactAdmin)
