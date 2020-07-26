from django.contrib import admin

# Register your models here.
from quran.models import *


@admin.register(Reciter)
class reciterAdmin(admin.ModelAdmin):
    list_display = ['id', 'r_nameFA', 'r_type', 'r_mode', 'r_create', 'r_update']
    # fieldsets = (
    #     (None, {'fields': ('r_nameAR', 'r_nameEN', 'r_nameFA')}),
    #     ('Names1', {'fields': ('r_url1', 'r_size1', 'r_quality1')}),
    #     ('Names2', {'fields': ('r_url2', 'r_size2', 'r_quality2')}),
    #     ('Names3', {'fields': ('r_url3','r_size3', 'r_quality3')}),
    # )


@admin.register(ReciterType)
class reciteTypeAdmin(admin.ModelAdmin):
    list_display = ['mode']
