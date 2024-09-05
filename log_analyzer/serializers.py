from rest_framework import serializers
from .models import SysmonLog

class SysmonLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysmonLog
        fields = ['id', 'json_data', 'timestamp', 'has_threat']
