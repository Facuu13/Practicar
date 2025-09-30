from django.db import models

# Create your models here.

class Sensor(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.valor})"

class Lectura(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    valor = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)

