from django.http import HttpResponse
from .models import Sensor, Lectura

# Create your views here.

def hello(request):
    return HttpResponse("Hola mundo")

def about(request):
    return HttpResponse("Pagina de about")

def mostrar_sensores(request):
    sensores = Sensor.objects.all()
    response = ", ".join([f"{sensor.nombre}: {sensor.valor}" for sensor in sensores])
    return HttpResponse(response)

def mostrar_sensor(request, sensor_id):
    s = Sensor.objects.get(id=sensor_id)
    return HttpResponse(f"Sensor: {s.nombre}, Valor: {s.valor}")
