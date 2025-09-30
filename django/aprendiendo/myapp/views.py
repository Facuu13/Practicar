from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("Hola mundo")

def about(request):
    return HttpResponse("Pagina de about")