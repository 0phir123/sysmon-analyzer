from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_log, name='upload_log'),
    path('logs/date/<str:start_date>/<str:end_date>/', views.get_logs_by_date, name='get_logs_by_date'),
    path('logs/<int:log_id>/', views.get_log_by_id, name='get_log_by_id'),
    path('logs/<int:log_id>/threat/', views.check_threat_by_id, name='check_threat_by_id'),
    path('logs/monthly-report/<int:year>/<int:month>/', views.monthly_threat_report, name='monthly_threat_report'),
]
