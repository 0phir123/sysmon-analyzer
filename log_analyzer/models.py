from django.db import models

class SysmonLog(models.Model):
    json_data = models.JSONField()  # Stores the entire log in JSON format
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of log creation
    has_threat = models.BooleanField(default=False)  # Indicates if the log contains a threat

    def __str__(self):
        return f"Log created on {self.timestamp}"
