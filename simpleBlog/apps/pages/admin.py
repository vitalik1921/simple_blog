from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from .models import Page


class PageAdmin(FlatPageAdmin):
    form = FlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites', 'add_name')}),
    )


admin.site.unregister(FlatPage)
admin.site.register(Page, PageAdmin)
