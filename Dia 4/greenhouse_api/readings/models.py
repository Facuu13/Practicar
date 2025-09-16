from django.db import models

class Reading(models.Model):
    device_id = models.CharField(max_length=50)
    ts_utc = models.DateTimeField()
    temp_c = models.DecimalField(max_digits=5, decimal_places=2)
    hum_pct = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.device_id} @ {self.ts_utc}"
