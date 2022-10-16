from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_email',
                    'query', 'date_time', 'response_sent')

    readonly_fields = (
        'contact_name',
        'contact_email',
        'query',
        'date_time',
        'message',
        'response_message',
        'response_sent')

    ordering = ('-date_time',)


admin.site.register(Contact, ContactAdmin)
