
---

## ❓ Preguntas y respuestas para entrevista

### 1. ¿Qué es Django y para qué se usa?

👉 Django es un **framework web en Python** que permite crear aplicaciones web de forma rápida, ordenada y segura.
Se usa para desarrollar desde páginas simples hasta sistemas grandes (ej: e-commerce, dashboards, APIs).

---

### 2. ¿Qué es el patrón MVC/MTV?

* MVC significa **Modelo - Vista - Controlador**.
* Django lo adapta a **MTV (Model - Template - View)**:

  * **Model**: define la estructura de los datos (como tablas en la base de datos).
  * **Template**: define cómo se muestran los datos en HTML.
  * **View**: maneja la lógica, recibe la petición del usuario y devuelve la respuesta.

---

### 3. ¿Cómo se conecta Django a una base de datos?

👉 En el archivo `settings.py` configuras la base de datos.
Por defecto viene con SQLite, pero podés usar MySQL o PostgreSQL.

Ejemplo para MySQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'greenhouse_db',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

### 4. ¿Qué es el ORM y qué ventaja tiene frente a SQL directo?

👉 ORM = *Object Relational Mapper*.
En vez de escribir queries SQL manuales (`SELECT * FROM sensores`), trabajás con objetos Python.

Ventaja: es más legible, seguro y funciona en varias bases de datos sin cambiar el código.

Ejemplo:

```python
# SQL directo
SELECT * FROM sensor WHERE temperatura > 25;

# Django ORM
sensores = Sensor.objects.filter(temperatura__gt=25)
```

---

### 5. ¿Qué diferencia hay entre una vista y un template?

* **Vista (View)**: contiene la lógica (ejemplo: leer datos de la base).
* **Template**: es la parte visual, HTML que se le muestra al usuario.

Ejemplo:

```python
# views.py
from django.shortcuts import render

def mostrar_sensor(request):
    datos = {"nombre": "Sensor1", "temp": 26.5}
    return render(request, "sensor.html", datos)
```

```html
<!-- sensor.html -->
<h1>Sensor: {{ nombre }}</h1>
<p>Temperatura: {{ temp }} °C</p>
```

---

## 📚 Explicación de los temas con ejemplos sencillos

### 🔹 1. Modelos (Models)

Son clases que representan tablas en la base de datos.

```python
from django.db import models

class Sensor(models.Model):
    nombre = models.CharField(max_length=50)
    temperatura = models.FloatField()
    humedad = models.FloatField()
```

➡️ Esto crea una tabla `Sensor` con tres columnas: `nombre`, `temperatura`, `humedad`.

---

### 🔹 2. Vistas (Views)

Son funciones o clases que responden a las solicitudes HTTP.

```python
from django.http import HttpResponse

def hola(request):
    return HttpResponse("Hola desde Django")
```

➡️ Si entrás en la URL `/hola/`, el navegador muestra “Hola desde Django”.

---

### 🔹 3. Templates

Son archivos HTML con variables dinámicas.

```html
<h1>Hola {{ usuario }}</h1>
<p>La temperatura es: {{ temperatura }} °C</p>
```

➡️ Si en la vista pasás `{"usuario": "Facu", "temperatura": 28}`, se muestra:
**Hola Facu – La temperatura es: 28 °C**

---

### 🔹 4. URLs

Conectan una dirección web con una vista.

```python
from django.urls import path
from . import views

urlpatterns = [
    path("hola/", views.hola),
    path("sensor/", views.mostrar_sensor),
]
```

---

### 🔹 5. ORM en acción

```python
# Crear un sensor
s = Sensor(nombre="Sensor1", temperatura=22.5, humedad=60)
s.save()

# Leer todos los sensores
todos = Sensor.objects.all()

# Filtrar
calientes = Sensor.objects.filter(temperatura__gt=25)
```

---


---

# 📌 Conceptos básicos de Django para entrevista

### 1. ¿Qué es Django?

* **Framework web en Python**.
* Permite crear apps rápido, seguras y mantenibles.
* Usa patrón **MTV (Model–Template–View)**.

👉 *Respuesta corta*:
“Django es un framework de Python que simplifica el desarrollo web, usando el patrón MTV: Modelos para la base de datos, Vistas para la lógica y Templates para la parte visual.”

---

### 2. Arquitectura MTV

* **Model** → define la estructura de datos (tablas).
* **Template** → define la interfaz (HTML).
* **View** → conecta todo, maneja la lógica de la petición.

👉 Ejemplo:
Un modelo `Sensor`, una vista `mostrar_sensor`, y un template `sensor.html`.

---

### 3. ORM (Object Relational Mapper)

* Permite interactuar con la base de datos con Python en vez de SQL.
* Ventaja: portabilidad entre bases y código más limpio.

👉 Ejemplo:

```python
# ORM Django
sensores = Sensor.objects.filter(temperatura__gt=25)
```

vs

```sql
-- SQL crudo
SELECT * FROM sensor WHERE temperatura > 25;
```

---

### 4. Ruteo de URLs

* Cada URL está vinculada a una vista.
* Se define en `urls.py`.

👉 Ejemplo:

```python
path("sensor/<int:id>/", views.sensor_detail)
```

---

### 5. Views

* Son funciones o clases que procesan una **request** y devuelven una **response**.
* Dos tipos:

  * **Function Based Views (FBV)**
  * **Class Based Views (CBV)**

👉 Ejemplo FBV:

```python
def hola(request):
    return HttpResponse("Hola Django")
```

---

### 6. Templates

* Archivos HTML con variables dinámicas (`{{ var }}`).
* Tienen un **lenguaje de plantillas** (loops, condiciones).

👉 Ejemplo:

```html
{% for s in sensores %}
  <p>{{ s.nombre }}: {{ s.temperatura }}</p>
{% endfor %}
```

---

### 7. Forms y Validación

* Django tiene un sistema de formularios para validar datos.
* Muy usado para crear/editar modelos.

👉 Ejemplo:

```python
from django import forms
class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['nombre', 'ubicacion']
```

---

### 8. Django Admin

* Panel automático para manejar datos.
* Gran diferencial de Django: levantar un CRUD sin código extra.

---

### 9. Migraciones

* Django traduce los `models.py` a SQL real.
* Comandos:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 10. Seguridad y Buenas Prácticas

* **Protección CSRF**: seguridad en formularios.
* **Autenticación**: sistema integrado de usuarios y permisos.
* **Settings**: `DEBUG`, `SECRET_KEY`, `ALLOWED_HOSTS`.

---

### 11. Django REST Framework (DRF) *(bonus, muy preguntado)*

* No es obligatorio, pero muchas empresas lo usan.
* Sirve para exponer APIs REST.
* En vez de HTML, devolvés JSON.

👉 Pregunta típica:
**“¿Cómo harías una API en Django?”**
Respuesta: “Con Django REST Framework puedo definir serializers para los modelos y vistas tipo APIView o ViewSets para exponer endpoints en JSON.”

---

### 12. Deployment (nivel conceptual)

* Podrían preguntarte cómo “subir” un proyecto.
* Básico: Django corre en un servidor (ej: Gunicorn + Nginx, Heroku, AWS).

👉 Respuesta corta:
“Django se despliega usando un servidor WSGI (como Gunicorn o uWSGI) detrás de un servidor web como Nginx. Para prototipos puede correrse en Heroku o Docker.”

---

# 📋 Preguntas comunes de entrevista (con respuestas breves)

1. **¿Qué diferencia hay entre Flask y Django?**
   👉 Flask es más liviano y flexible, Django es más completo (admin, ORM, seguridad, plantillas).

2. **¿Qué es una migración en Django?**
   👉 Es un archivo que traduce los modelos de Python a SQL para sincronizar la base de datos.

3. **¿Qué ventajas tiene usar ORM sobre SQL directo?**
   👉 Evita errores, es más portable y seguro contra inyección SQL.

4. **¿Cómo manejarías un formulario en Django?**
   👉 Con Django Forms o ModelForms, que validan y guardan datos en la base.

5. **¿Qué son los middlewares?**
   👉 Código que se ejecuta antes o después de cada request/response (ej: autenticación, logging, compresión).

6. **¿Cómo protegerías una vista para que solo usuarios logueados la vean?**
   👉 Usando el decorador `@login_required` o permisos en CBV.

7. **¿Qué son las señales (signals)?**
   👉 Callbacks que se disparan cuando ocurre un evento (ej: `post_save` cuando se guarda un modelo).

---

# 🚀 Estrategia si no tenés experiencia real

Podés contestar así en la entrevista:

> “No trabajé directamente en producción con Django, pero entiendo su arquitectura MTV, el uso de modelos con ORM, vistas y templates. Estuve practicando un mini-proyecto IoT en Django, así que me resulta familiar cómo estructurar una app y cómo manejar datos desde una base de datos hasta la web. Además, como tengo experiencia en Python y bases de datos, me adapto rápido.”

---


¡Entendido! 🙌
Vamos a ir **pieza por pieza**, para que todo te quede bien claro. Empezamos con lo primero y más importante en Django: **`models.py`**.

---

# 📌 ¿Qué es `models.py` en Django?

* Es el archivo donde definís tus **modelos de datos**.
* Un **modelo** en Django es una **clase de Python** que representa una **tabla en la base de datos**.
* Cada **atributo de la clase** representa una **columna de la tabla**.

👉 Django se encarga de traducir esas clases a SQL usando el **ORM (Object-Relational Mapper)**.

---

# 📊 Ejemplo básico

Archivo: `sensores/models.py`

```python
from django.db import models

class Sensor(models.Model):
    nombre = models.CharField(max_length=50)
    valor = models.IntegerField()
```

Esto significa:

* Clase **Sensor** → tabla `sensores_sensor` en la base de datos (Django agrega el nombre de la app antes).
* Campo `nombre` → columna de tipo texto (`VARCHAR(50)`).
* Campo `valor` → columna de tipo entero (`INT`).
* Django automáticamente crea un campo `id` como **clave primaria (primary key)**.

---

# 🛠️ Tipos de campos comunes

Django tiene muchos tipos de campos (`Field`), algunos son:

* `CharField(max_length=…)` → texto corto.
* `TextField()` → texto largo.
* `IntegerField()` → enteros.
* `FloatField()` → números decimales.
* `BooleanField()` → True/False.
* `DateTimeField(auto_now_add=True)` → fecha/hora al crear.
* `ForeignKey()` → relación con otra tabla.

👉 Ejemplo con varios campos:

```python
class Lectura(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    valor = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)
```

Esto crea una tabla de lecturas donde cada fila está vinculada a un sensor.

---

# ⚡ Cómo usar los modelos (ORM)

Después de definirlos, corrés:

```bash
python manage.py makemigrations
python manage.py migrate
```

Esto crea las tablas en la DB.
Luego podés usar el ORM desde el **shell de Django**:

```bash
python manage.py shell
```

```python
from sensores.models import Sensor

# Crear un sensor
s = Sensor(nombre="Temperatura", valor=25)
s.save()

# Consultar todos
Sensor.objects.all()
# → <QuerySet [<Sensor: Sensor object (1)>]>

# Filtrar
Sensor.objects.filter(valor__gt=20)
```

👉 El ORM traduce tus comandos Python a SQL automáticamente.

---

# ✅ Resumen de `models.py`

* Define la **estructura de tus datos** (tablas y columnas).
* Cada clase = una tabla.
* Cada atributo = una columna.
* Se usa junto con el ORM para crear, leer, actualizar y borrar datos sin escribir SQL.

---

# 📌 ¿Qué es `views.py` en Django?

* Es el archivo donde definís las **vistas** de tu aplicación.
* Una **vista** es simplemente una función (o clase) que recibe un **request HTTP** y devuelve una **response HTTP**.
* Piensalo así:

  * **URL** → llama a una **vista** → que procesa lógica y devuelve algo (HTML, JSON, texto, etc.).

👉 En backend puro, la vista suele devolver **JSON**.

---

# 👨‍💻 Ejemplo 1: Vista como función

Archivo: `myapp/views.py`

```python
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("Hola desde Django")
```

* Recibe un `request` (lo que envía el navegador o cliente).
* Devuelve un `HttpResponse` con un texto.
* Si lo conectás a una URL, al entrar en el navegador vas a ver ese texto.

---

# 👨‍💻 Ejemplo 2: Vista que usa el modelo

Supongamos que ya tenemos el modelo `Sensor`.

```python
from django.http import HttpResponse
from .models import Sensor

def mostrar_sensores(request):
    sensores = Sensor.objects.all()
    texto = ", ".join([f"{s.nombre}: {s.valor}" for s in sensores])
    return HttpResponse(texto)
```

👉 Paso a paso:

1. `Sensor.objects.all()` consulta la DB.
2. Arma un string con los datos.
3. Lo devuelve como texto plano.

---

# 👩‍🏫 Tipos de vistas

En Django hay **dos estilos**:

1. **Function-Based Views (FBV)** → como los ejemplos de arriba.

   * Simples, fáciles para empezar.

2. **Class-Based Views (CBV)** → vistas como clases, con métodos (`get`, `post`, etc.).
   Ejemplo:

   ```python
   from django.http import JsonResponse
   from django.views import View
   from .models import Sensor

   class SensorList(View):
       def get(self, request):
           sensores = list(Sensor.objects.values())
           return JsonResponse(sensores, safe=False)
   ```

   * `get` maneja peticiones GET.
   * `post` manejaría POST, etc.
   * Se usan mucho en proyectos grandes porque son más ordenadas y reusables.

---

# ✅ Resumen de `views.py`

* Acá va la **lógica** de tu aplicación.
* Cada vista recibe un `request` y devuelve una `response`.
* Podés usarlas como función o como clase.
* Normalmente se conectan a los modelos (`models.py`) para devolver datos.

---

# 📌 ¿Qué es el ORM?

* **ORM = Object Relational Mapper**.
* Te permite trabajar con la **base de datos usando objetos de Python**, sin tener que escribir SQL directamente.
* Ventaja: código más limpio, portable (funciona con SQLite, PostgreSQL, MySQL, etc. sin cambiar nada).

👉 Ejemplo SQL vs ORM:

SQL:

```sql
SELECT * FROM sensor WHERE valor > 20;
```

ORM:

```python
Sensor.objects.filter(valor__gt=20)
```

---

# 👨‍💻 Ejemplos básicos con el ORM

## 1. Crear registros

```python
# Forma larga
s = Sensor(nombre="temp1", valor=25)
s.save()

# Forma corta
Sensor.objects.create(nombre="hum1", valor=60)
```

---

## 2. Leer registros

```python
# Todos los registros
Sensor.objects.all()

# Filtrar (WHERE)
Sensor.objects.filter(valor__gt=20)     # valor > 20
Sensor.objects.filter(nombre="temp1")   # nombre = 'temp1'

# Uno solo (si existe)
Sensor.objects.get(id=1)   # trae el sensor con id=1
```

⚠️ `get` lanza error si no encuentra nada o hay más de uno.
En cambio `filter` devuelve un queryset (lista).

---

## 3. Actualizar registros

```python
s = Sensor.objects.get(id=1)
s.valor = 30
s.save()
```

---

## 4. Borrar registros

```python
s = Sensor.objects.get(id=1)
s.delete()
```

---

# 📊 Consultas más útiles

* Comparadores:

  * `__gt` → mayor que
  * `__lt` → menor que
  * `__gte` → mayor o igual
  * `__lte` → menor o igual
  * `__contains` → contiene (como `LIKE`)
  * `__startswith` → empieza con

Ejemplo:

```python
Sensor.objects.filter(nombre__startswith="t")
```

* Ordenar resultados:

```python
Sensor.objects.all().order_by("valor")     # ascendente
Sensor.objects.all().order_by("-valor")    # descendente
```

* Limitar resultados:

```python
Sensor.objects.all()[:5]   # los primeros 5
```

---

# ✅ Resumen

* El **ORM** reemplaza SQL por métodos de Python.
* Lo más usado: `create`, `all`, `filter`, `get`, `update`, `delete`.
* Tiene comparadores (`__gt`, `__lt`, etc.) y ordenaciones (`order_by`).

---

¡Genial, Facu! 🙌
Entonces seguimos con el siguiente bloque importante: **`urls.py`**.

---

# 📌 ¿Qué es `urls.py` en Django?

* Es el archivo donde definís las **rutas de tu aplicación web**.
* Una **ruta (URL)** indica qué vista (`views.py`) se debe ejecutar cuando alguien accede a cierta dirección.
* Ejemplo:

  * Entrás a `http://127.0.0.1:8000/sensores/`
  * Django busca en `urls.py`
  * Ejecuta la vista que le corresponde → devuelve la respuesta.

👉 En pocas palabras: **URLs conectan el navegador/cliente con las vistas**.

---

# 🗂️ Tipos de `urls.py`

Django maneja dos niveles:

1. **urls.py del proyecto** (en la carpeta principal):

   * Centraliza todas las apps.
2. **urls.py de cada app** (ej: `myapp/urls.py`):

   * Define las rutas específicas de esa app.

---

# 👨‍💻 Ejemplo 1: URL simple

En `myapp/views.py` tenés:

```python
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("Hola desde Django")
```

En `myapp/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("hola/", views.hola_mundo),
]
```

En `mi_proyecto/urls.py` (global):

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("myapp.urls")),   # incluye las rutas de la app
]
```

👉 Ahora si vas a `http://127.0.0.1:8000/hola/`, ves el texto de la vista.

---

# 👨‍💻 Ejemplo 2: URL con parámetros

Podés capturar valores de la URL para usarlos en la vista.

En `myapp/views.py`:

```python
from django.http import HttpResponse

def mostrar_sensor(request, sensor_id):
    return HttpResponse(f"Mostrando el sensor con id {sensor_id}")
```

En `myapp/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("sensor/<int:sensor_id>/", views.mostrar_sensor),
]
```

👉 Si entrás a `http://127.0.0.1:8000/sensor/5/` → devuelve `"Mostrando el sensor con id 5"`.

---

# 👩‍🏫 Cosas a tener en cuenta

* `path("texto/", …)` → URL fija.
* `path("<int:id>/", …)` → parámetro numérico.
* `path("<str:nombre>/", …)` → parámetro string.
* Usá `include()` para organizar mejor las rutas de cada app.

---

# ✅ Resumen de `urls.py`

* Es el “mapa” de la aplicación.
* Conecta **URL → Vista**.
* Podés definir rutas fijas o con parámetros.
* Se divide en **urls globales** (proyecto) y **urls locales** (app).

---

# 📌 ¿Qué es `serializers.py`?

* Es el archivo donde definís los **serializadores**.
* Un **serializer** convierte:

  * Objetos de Django (ej: un `Sensor`) → JSON (para enviar al cliente).
  * JSON recibido en un request → objeto de Django (para guardar en la DB).
* Es el puente entre el **modelo** y el **mundo exterior** (navegador, Postman, app móvil, etc.).

👉 Sin serializer, no podés trabajar cómodamente con JSON.

---

# 👨‍💻 Ejemplo básico

En `sensores/serializers.py`:

```python
from rest_framework import serializers
from .models import Sensor

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'nombre', 'valor']
```

Explicación:

* `SensorSerializer` → define cómo se transforma un `Sensor`.
* `model = Sensor` → se basa en ese modelo.
* `fields = [...]` → qué campos incluir en el JSON.

---

# 🔄 Cómo se usa

En una vista (ejemplo simplificado):

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Sensor
from .serializers import SensorSerializer

@api_view(['GET'])
def listar_sensores(request):
    sensores = Sensor.objects.all()
    serializer = SensorSerializer(sensores, many=True)
    return Response(serializer.data)
```

👉 Paso a paso:

1. Traemos todos los sensores.
2. El serializer los transforma a JSON (`serializer.data`).
3. Lo devolvemos en la response.

---

# 👨‍💻 Ejemplo de entrada JSON → objeto

Supongamos que hacemos un **POST** con:

```json
{
  "nombre": "humedad",
  "valor": 65
}
```

En la vista:

```python
@api_view(['POST'])
def crear_sensor(request):
    serializer = SensorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # crea el Sensor en la DB
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
```

👉 El serializer valida los datos y los guarda.

---

# 🔑 Ventajas de los serializers

* Validan automáticamente (ej: que `valor` sea un número).
* Evitan tener que armar JSON a mano.
* Integran fácil con **views genéricas** (`ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`).

---

# ✅ Resumen

* `serializers.py` convierte **Model ↔ JSON**.
* Facilita tanto leer (GET) como crear/actualizar datos (POST/PUT).
* Es la pieza clave para que Django se comporte como un **backend/API REST**.

---


