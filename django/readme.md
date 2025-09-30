
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

