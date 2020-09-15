from django.contrib import admin

# Register your models here.
from quran.models import *


@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    list_display = ['count', 'type']


@admin.register(TafTar)
class TafTarAdmin(admin.ModelAdmin):
    list_display = ['titleFA', 'db_name', 'type', 'mode', 'create', 'update', 'order',
                    'reciter_id']

@admin.register(Reciter)
class reciterAdmin(admin.ModelAdmin):
    # list_display = ['id', 'r_nameFA', 'r_type', 'r_mode']
    list_display = [ 'r_nameFA','r_nameAR', 'r_type', 'r_mode', 'r_create', 'r_update']
    list_filter = ('r_mode', 'r_type')
    search_fields = ['r_nameFA', 'r_type']

    # fieldsets = (
    #     (None, {'fields': ('r_nameAR', 'r_nameEN', 'r_nameFA')}),
    #     ('Names1', {'fields': ('r_url1', 'r_size1', 'r_quality1')}),
    #     ('Names2', {'fields': ('r_url2', 'r_size2', 'r_quality2')}),
    #     ('Names3', {'fields': ('r_url3','r_size3', 'r_quality3')}),
    # )
