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