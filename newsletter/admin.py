from django.contrib import admin
from .models import Newsletter


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'uid')
    ordering = ('name',)


admin.site.register(Newsletter, NewsletterAdmin)
