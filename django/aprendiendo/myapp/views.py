from django.http import HttpResponse
from .models import Sensor, Lectura
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SensorSerializer

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


@api_view(['GET'])
def listar_sensores(request):
    sensores = Sensor.objects.all()
    serializer = SensorSerializer(sensores, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crear_sensor(request):
    serializer = SensorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # crea el Sensor en la DB
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)