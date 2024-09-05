from django.contrib import admin
from .models import SysmonLog

@admin.register(SysmonLog)
class SysmonLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'has_threat')
    search_fields = ['json_data']
    list_filter = ['has_threat']
