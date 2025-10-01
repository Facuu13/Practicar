from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Sensor
from .serializers import SensorSerializer
# Create your views here.

def hello(request):
    return HttpResponse("Hola mundo")

def listar_sensores(request):
    sensores = Sensor.objects.all()
    response = ", ".join([f"{sensor.name}: {sensor.valor}" for sensor in sensores])
    return HttpResponse(response)

@api_view(['GET', 'POST'])
def sensor_list_create(request):
    if request.method == 'GET':
        sensores = Sensor.objects.all().order_by('-created_at')
        serializer = SensorSerializer(sensores, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)