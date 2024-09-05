from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SysmonLogSerializer
from .models import SysmonLog
from django.utils.dateparse import parse_datetime
import json


INDICATORS = ["mimikatz", "lsass", "sam"]  # Threat indicators

def analyze_log(json_data):
    for key, value in json_data.items():
        if any(indicator in str(value).lower() for indicator in INDICATORS):
            return True
    return False

@api_view(['POST'])
def upload_log(request):
    data = request.data
    has_threat = analyze_log(data)
    sysmon_log = SysmonLog.objects.create(json_data=data, has_threat=has_threat)
    return Response({"id": sysmon_log.id, "has_threat": sysmon_log.has_threat}, status=201)




@api_view(['GET'])
def get_logs_by_date(request, start_date, end_date):
    start = parse_datetime(start_date)
    end = parse_datetime(end_date)
    logs = SysmonLog.objects.filter(timestamp__range=[start, end])
    if logs.exists():
        return Response(SysmonLogSerializer(logs, many=True).data)
    else:
        return Response({"message": "No logs found in this date range"}, status=404)


@api_view(['GET'])
def get_log_by_id(request, log_id):
    try:
        log = SysmonLog.objects.get(id=log_id)
        return Response(SysmonLogSerializer(log).data)
    except SysmonLog.DoesNotExist:
        return Response({"message": "Log not found"}, status=404)


@api_view(['GET'])
def check_threat_by_id(request, log_id):
    try:
        log = SysmonLog.objects.get(id=log_id)
        return Response({"id": log.id, "has_threat": log.has_threat})
    except SysmonLog.DoesNotExist:
        return Response({"message": "Log not found"}, status=404)


from django.db.models import Count
from django.utils.dateparse import parse_datetime

import calendar
from datetime import datetime

@api_view(['GET'])
def monthly_threat_report(request, year, month):
    # Get the last day of the month
    last_day = calendar.monthrange(year, month)[1]  # This gives the last day of the month

    # Construct the start and end dates
    start_date = f"{year}-{month}-01T00:00:00"
    end_date = f"{year}-{month}-{last_day}T23:59:59"
    
    # Parse the dates to datetime objects
    start = parse_datetime(start_date)
    end = parse_datetime(end_date)
    
    # Filter logs by date range and check if there were any threats
    logs = SysmonLog.objects.filter(timestamp__range=[start, end], has_threat=True)
    
    if not logs.exists():
        return Response({"message": "No threat logs found for this month"}, status=404)
    
    # Count the number of threats
    threat_count = logs.count()
    
    return Response({
        "month": f"{year}-{month}",
        "threat_count": threat_count,
        "logs": SysmonLogSerializer(logs, many=True).data
    })
