from django.contrib import admin
from .models import Newsletter


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('newsletter_name', 'newsletter_email', 'uid')
    ordering = ('newsletter_name',)


admin.site.register(Newsletter, NewsletterAdmin)
