from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    valor = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
