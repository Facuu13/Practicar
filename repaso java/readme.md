
---

## 🟦 ¿Qué es Java?

* Es un **lenguaje de programación orientado a objetos (OOP)**.
* Se compila a **bytecode** (archivos `.class`) y se ejecuta en la **JVM (Java Virtual Machine)**.
* Lema clásico: *"Write once, run anywhere"* (es portable).

---

## 🟦 Estructura básica de un programa Java

Siempre arranca con una **clase** y un método principal `main`:

```java
public class Hola {
    public static void main(String[] args) {
        System.out.println("Hola mundo!");
    }
}
```

* `public class Hola`: define una clase llamada `Hola`.
* `public static void main(String[] args)`: punto de entrada, el método que se ejecuta al iniciar.
* `System.out.println(...)`: imprime en consola.

---

## 🟦 Tipos de datos básicos

* **int** → números enteros.
* **double** → decimales.
* **boolean** → `true` o `false`.
* **String** → cadenas de texto.

Ejemplo:

```java
int edad = 30;
double altura = 1.75;
boolean activo = true;
String nombre = "Facundo";

System.out.println("Me llamo " + nombre + " y tengo " + edad + " años.");
```

---

## 🟦 Control de flujo

Como en C/Python, pero con sintaxis más estricta.

```java
int num = 5;

if (num > 0) {
    System.out.println("Es positivo");
} else {
    System.out.println("Es negativo o cero");
}

for (int i = 0; i < 3; i++) {
    System.out.println("i = " + i);
}
```

---

## 🟦 Funciones (métodos)

Se definen dentro de una clase:

```java
public class Calculadora {
    // Método que suma dos enteros
    public static int sumar(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        int resultado = sumar(4, 6);
        System.out.println("Resultado: " + resultado);
    }
}
```

---

## 🟦 Programación orientada a objetos

* Todo en Java está dentro de una **clase**.
* Podés crear objetos con **constructores** y **atributos**.

```java
class Persona {
    String nombre;
    int edad;

    // Constructor
    Persona(String n, int e) {
        nombre = n;
        edad = e;
    }

    void presentarse() {
        System.out.println("Hola, soy " + nombre + " y tengo " + edad + " años.");
    }
}

public class Main {
    public static void main(String[] args) {
        Persona p1 = new Persona("Facundo", 30);
        p1.presentarse();
    }
}
```

---

👉 En resumen:

* Todo está en **clases**.
* Los programas empiezan en `public static void main`.
* Tipado fuerte (hay que declarar tipos).
* Usa **POO** (objetos, métodos, constructores, herencia, etc.).

---

¡Genial! 🚀 Te armo una **chuleta rápida de Java** con ejemplos sencillos para que lo recuerdes fácil, como si fuese un machete de repaso.

---

# 📝 Chuleta rápida de Java

---

## 🔹 Estructura básica

```java
public class Hola {
    public static void main(String[] args) {
        System.out.println("Hola Mundo!");
    }
}
```

---

## 🔹 Tipos de datos

```java
int edad = 30;          // Entero
double altura = 1.75;   // Decimal
boolean activo = true;  // Booleano
char inicial = 'F';     // Un carácter
String nombre = "Facu"; // Cadena
```

---

## 🔹 Operadores

```java
int a = 5, b = 2;

int suma = a + b;        // 7
int resta = a - b;       // 3
int mult = a * b;        // 10
int div = a / b;         // 2 (entero)
double divReal = 5.0/2;  // 2.5

boolean comp = (a > b);  // true
boolean log = (a > 0 && b > 0); // true
```

---

## 🔹 Condicionales

```java
int num = 10;

if (num > 0) {
    System.out.println("Positivo");
} else if (num < 0) {
    System.out.println("Negativo");
} else {
    System.out.println("Cero");
}
```

---

## 🔹 Bucles

```java
// For
for (int i = 0; i < 3; i++) {
    System.out.println("i = " + i);
}

// While
int j = 0;
while (j < 3) {
    System.out.println("j = " + j);
    j++;
}
```

---

## 🔹 Métodos (funciones)

```java
public class Calculadora {
    public static int sumar(int x, int y) {
        return x + y;
    }

    public static void main(String[] args) {
        int res = sumar(3, 4);
        System.out.println("Resultado = " + res);
    }
}
```

---

## 🔹 Clases y Objetos

```java
class Persona {
    String nombre;
    int edad;

    // Constructor
    Persona(String n, int e) {
        nombre = n;
        edad = e;
    }

    void presentarse() {
        System.out.println("Soy " + nombre + ", edad " + edad);
    }
}

public class Main {
    public static void main(String[] args) {
        Persona p1 = new Persona("Facu", 30);
        p1.presentarse(); // Soy Facu, edad 30
    }
}
```

---

## 🔹 Arrays

```java
int[] numeros = {10, 20, 30};
System.out.println(numeros[0]); // 10

for (int n : numeros) {
    System.out.println(n);
}
```

---

## 🔹 Strings

```java
String saludo = "Hola";
System.out.println(saludo.length());      // 4
System.out.println(saludo.toUpperCase()); // HOLA
System.out.println(saludo + " Mundo");    // Hola Mundo
```

---

📌 Con esta chuleta tenés lo esencial para:

* **Variables**
* **Condicionales**
* **Bucles**
* **Métodos**
* **Clases/Objetos**
* **Arrays y Strings**

---


## 🔹 Diferencia entre `for` normal y `for-each`

### For normal (con índice):

```java
int[] numeros = {10, 20, 30};

for (int i = 0; i < numeros.length; i++) {
    System.out.println("Índice " + i + ": " + numeros[i]);
}
```

👉 Controlás el índice (`i`), podés modificar elementos, saltarte algunos, etc.

---

### For-each (más simple):

```java
int[] numeros = {10, 20, 30};

for (int n : numeros) {
    System.out.println("Elemento: " + n);
}
```

👉 No ves el índice, solo cada valor. Es más limpio cuando querés **leer/usar datos**, no cambiarlos.

---

## 🔹 Colecciones en Java (además de arrays)

Con los arrays estás limitado a un tamaño fijo. Java tiene la librería **Collections** (`ArrayList`, `HashMap`, etc.), mucho más usada en proyectos reales.

Ejemplo con **ArrayList**:

```java
import java.util.ArrayList;

public class EjemploLista {
    public static void main(String[] args) {
        ArrayList<String> frutas = new ArrayList<>();

        frutas.add("Manzana");
        frutas.add("Banana");
        frutas.add("Naranja");

        // For-each
        for (String f : frutas) {
            System.out.println(f);
        }

        // Acceso por índice
        System.out.println("Primera fruta: " + frutas.get(0));
    }
}
```

---

## 🔹 Un poco más de POO (herencia)

Ya vimos clases y objetos, ahora te muestro cómo funciona **herencia**:

```java
class Animal {
    void sonido() {
        System.out.println("El animal hace un sonido");
    }
}

class Perro extends Animal {
    @Override
    void sonido() {
        System.out.println("El perro ladra");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal a = new Animal();
        a.sonido(); // El animal hace un sonido

        Perro p = new Perro();
        p.sonido(); // El perro ladra
    }
}
```

👉 `extends` significa que `Perro` hereda de `Animal`.
👉 Podés sobreescribir métodos (`@Override`).

---

📌 Hasta acá ya repasamos:

* Estructura básica
* Variables y tipos
* Condicionales
* Bucles (`for`, `while`, `for-each`)
* Clases, objetos, constructores
* Arrays y colecciones
* Herencia

---

¡Perfecto, Facu! 👌
Te explico esas cositas que aparecieron en el código, porque son parte del “core” de Java orientado a objetos. Te las voy a dar **una por una, con ejemplos sencillos** para que no quede ninguna duda.

---

# 🔹 1. `this`

👉 **Hace referencia al objeto actual** (a sí mismo).
Sirve para distinguir atributos de variables locales, o para pasarse como referencia.

```java
class Persona {
    String nombre;

    Persona(String nombre) {
        this.nombre = nombre;  // diferencia entre el atributo y el parámetro
    }

    void presentarse() {
        System.out.println("Hola, soy " + this.nombre);
    }
}

public class Main {
    public static void main(String[] args) {
        Persona p = new Persona("Facu");
        p.presentarse();  // Hola, soy Facu
    }
}
```

Si no usás `this`, en casos de nombres iguales, Java se confunde entre el atributo y el parámetro.

---

# 🔹 2. `super`

👉 **Hace referencia a la clase padre**.
Se usa para:

* Llamar al constructor de la clase padre.
* Acceder a métodos o atributos heredados.

```java
class Animal {
    String nombre;

    Animal(String nombre) {
        this.nombre = nombre;
    }

    void hacerSonido() {
        System.out.println("El animal hace un sonido");
    }
}

class Perro extends Animal {
    Perro(String nombre) {
        super(nombre); // llama al constructor de Animal
    }

    @Override
    void hacerSonido() {
        super.hacerSonido(); // llama al método de la clase padre
        System.out.println("El perro ladra");
    }
}

public class Main {
    public static void main(String[] args) {
        Perro p = new Perro("Firulais");
        p.hacerSonido();
        // El animal hace un sonido
        // El perro ladra
    }
}
```

---

# 🔹 3. `protected`

👉 Es un **modificador de acceso**.
Define **quién puede acceder** a una variable o método.

* `public` → todos (dentro y fuera de la clase).
* `private` → solo dentro de la misma clase.
* `protected` → solo dentro de la misma clase **y sus subclases**.
* *(sin nada)* → solo dentro del mismo *package*.

Ejemplo:

```java
class Animal {
    protected String nombre; // accesible en la subclase

    Animal(String nombre) {
        this.nombre = nombre;
    }
}

class Perro extends Animal {
    Perro(String nombre) {
        super(nombre);
    }

    void mostrar() {
        System.out.println("Soy un perro y me llamo " + nombre); // puedo acceder
    }
}
```

Si el atributo hubiera sido `private`, la subclase no podría acceder directo a `nombre`.

---

# 🔹 4. `abstract class`

👉 Una **clase abstracta** es una clase que **no se puede instanciar directamente**, solo sirve como “molde” para otras clases.
Puede tener métodos **abstractos** (sin cuerpo) que las subclases deben implementar.

```java
abstract class Figura {
    abstract double area();  // cada figura debe implementar cómo calcula el área
}

class Circulo extends Figura {
    double radio;

    Circulo(double r) {
        this.radio = r;
    }

    @Override
    double area() {
        return Math.PI * radio * radio;
    }
}

public class Main {
    public static void main(String[] args) {
        // Figura f = new Figura(); // ❌ no se puede
        Circulo c = new Circulo(3);
        System.out.println("Área del círculo: " + c.area());
    }
}
```

👉 Sirve para definir una especie de **contrato**: “todas las subclases deben implementar esto”.

---

## 🔹 En resumen

* **`this`** → se refiere al objeto actual.
* **`super`** → referencia a la clase padre (constructor/métodos).
* **`protected`** → acceso limitado a la clase y sus subclases.
* **`abstract class`** → clases que no se pueden instanciar, usadas como molde para herencia.

---
¡Perfecto! 🚀 Te armo un **kit completo para entrevistas en Java**, con **preguntas típicas + respuestas claras**, más unos **ejemplos cortitos de código** para que no te olvides.

---

# 📝 Top 10 Preguntas y Respuestas de Java en Entrevistas

---

## 🔹 1. ¿Cuál es la diferencia entre `==` y `.equals()`?

* `==` compara **referencias de memoria** (si apuntan al mismo objeto).
* `.equals()` compara **contenido lógico** (por ejemplo, si dos Strings tienen las mismas letras).

```java
String a = new String("hola");
String b = new String("hola");

System.out.println(a == b);       // false (objetos distintos)
System.out.println(a.equals(b));  // true  (contenido igual)
```

---

## 🔹 2. ¿Qué es una clase y un objeto?

* **Clase**: plantilla que define atributos y métodos.
* **Objeto**: instancia concreta de esa clase.

```java
class Persona {
    String nombre;
    int edad;
}

Persona p = new Persona();  // objeto
```

---

## 🔹 3. ¿Qué es herencia en Java?

Permite que una clase “hija” use atributos y métodos de una clase “padre”.

```java
class Animal {
    void sonido() { System.out.println("Hace un sonido"); }
}

class Perro extends Animal {
    void sonido() { System.out.println("Ladra"); }
}
```

👉 Pregunta derivada: *¿Qué es polimorfismo?*
Es cuando un mismo método se comporta distinto según el objeto.

```java
Animal a = new Perro();
a.sonido(); // Ladra
```

---

## 🔹 4. Diferencia entre **clase abstracta** e **interface**

* **Abstract class**: puede tener métodos implementados y abstractos.
* **Interface**: solo define métodos (contratos), la clase que la implemente debe definirlos todos.
* Una clase solo puede heredar **una clase abstracta**, pero puede implementar **múltiples interfaces**.

---

## 🔹 5. Diferencia entre `Array` y `ArrayList`

* `Array`: tamaño fijo.
* `ArrayList`: dinámico, crece automáticamente.

```java
int[] arr = {1,2,3};
ArrayList<Integer> lista = new ArrayList<>();
lista.add(1);
lista.add(2);
```

---

## 🔹 6. ¿Cómo se maneja una excepción en Java?

Con `try`, `catch` y opcional `finally`.

```java
try {
    int x = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Error: " + e.getMessage());
} finally {
    System.out.println("Esto siempre se ejecuta");
}
```

---

## 🔹 7. ¿Qué diferencia hay entre JDK, JRE y JVM?

* **JVM**: Java Virtual Machine → ejecuta el bytecode.
* **JRE**: Java Runtime Environment → JVM + librerías necesarias para correr programas.
* **JDK**: Java Development Kit → JRE + compilador y herramientas de desarrollo.

---

## 🔹 8. ¿Qué son los modificadores de acceso?

* `public`: todos pueden acceder.
* `private`: solo la misma clase.
* `protected`: la clase + subclases.
* *default* (sin palabra clave): solo dentro del mismo *package*.

---

## 🔹 9. ¿Qué es el Garbage Collector?

Es el mecanismo de Java que **libera memoria automáticamente** cuando los objetos ya no son referenciados.

---

## 🔹 10. ¿Cómo se crea un hilo (thread) en Java?

Dos formas:

1. Extendiendo `Thread`.
2. Implementando `Runnable`.

```java
class MiHilo extends Thread {
    public void run() {
        System.out.println("Hilo corriendo...");
    }
}

new MiHilo().start();
```

---

# 🟢 Extra: Preguntas rápidas de repaso

* **¿Qué es `static`?** → significa que pertenece a la clase, no al objeto. Ej: `Math.sqrt()`.
* **¿Qué es sobrecarga (overloading)?** → varios métodos con el mismo nombre pero distinta firma (parámetros).
* **¿Qué es sobreescritura (overriding)?** → redefinir un método heredado en una subclase.
* **¿Qué es un constructor?** → método especial que se ejecuta al crear un objeto.
* **¿Qué es `final`?** → si es una variable → constante; si es un método → no se puede sobreescribir; si es una clase → no se puede heredar.

---

# 🟦 Mini-desafíos que suelen dar en entrevistas

1. **Invertir un String**

```java
String s = "hola";
String invertido = new StringBuilder(s).reverse().toString();
System.out.println(invertido); // aloh
```

2. **Encontrar el mayor número en un array**

```java
int[] nums = {5, 9, 3, 7};
int max = nums[0];
for (int n : nums) {
    if (n > max) max = n;
}
System.out.println(max); // 9
```

3. **Contar cuántas veces aparece una palabra en un texto**

```java
String texto = "hola hola chau hola";
String[] palabras = texto.split(" ");
int count = 0;
for (String p : palabras) {
    if (p.equals("hola")) count++;
}
System.out.println(count); // 3
```

---

📌 Con todo esto cubrís lo más común que preguntan en entrevistas:

* Sintaxis básica.
* POO (clases, objetos, herencia, polimorfismo).
* Colecciones (`ArrayList`, `HashMap`).
* Excepciones.
* JVM/JDK/JRE.
* Threads (al menos de forma conceptual).

---
¡Bien visto! 👌
Vamos paso a paso:

---

# 🔹 ¿Qué es `var entry` en el `for`?

En Java **a partir de la versión 10** existe `var`, que permite que el compilador **infiere el tipo automáticamente**.

Ejemplo con HashMap:

```java
HashMap<String, Integer> edades = new HashMap<>();
edades.put("Ana", 25);

for (var entry : edades.entrySet()) {
    // El compilador entiende que "entry" es de tipo Map.Entry<String, Integer>
    System.out.println(entry.getKey() + " -> " + entry.getValue());
}
```

👉 `var` es solo azúcar sintáctica:

* En lugar de escribir **largo**:

```java
for (Map.Entry<String, Integer> entry : edades.entrySet()) { ... }
```

* Usás **corto**:

```java
for (var entry : edades.entrySet()) { ... }
```

📌 Importante: `var` **no es dinámico** como en Python o JavaScript; el tipo se determina en compilación y no cambia.

---

# 🔹 Comparativa rápida: ArrayList vs HashMap vs HashSet

| Estructura    | Qué guarda                                   | Clave única                 | Permite duplicados | Acceso típico                    | Ejemplo de uso                                    |
| ------------- | -------------------------------------------- | --------------------------- | ------------------ | -------------------------------- | ------------------------------------------------- |
| **ArrayList** | Lista ordenada de elementos (índice → valor) | ❌                           | ✅                  | Por índice (`get(i)`)            | Lista de nombres en orden de llegada              |
| **HashMap**   | Pares clave → valor                          | ✅ (una sola vez cada clave) | ✅ (valores)        | Por clave (`get(k)`)             | Guardar la edad de cada persona (`nombre → edad`) |
| **HashSet**   | Conjunto de valores únicos (sin orden)       | N/A                         | ❌                  | Verificación rápida (`contains`) | Lista de emails únicos, sin duplicados            |

---

# 🔹 Ejemplos cortitos

### ArrayList

```java
import java.util.ArrayList;
ArrayList<String> lista = new ArrayList<>();
lista.add("Ana");
lista.add("Juan");
lista.add("Ana"); // ✅ permite duplicado
System.out.println(lista); // [Ana, Juan, Ana]
```

### HashMap

```java
import java.util.HashMap;
HashMap<String, Integer> edades = new HashMap<>();
edades.put("Ana", 25);
edades.put("Ana", 30); // ⚠️ sobrescribe valor
System.out.println(edades); // {Ana=30}
```

### HashSet

```java
import java.util.HashSet;
HashSet<String> emails = new HashSet<>();
emails.add("a@gmail.com");
emails.add("b@gmail.com");
emails.add("a@gmail.com"); // ❌ duplicado ignorado
System.out.println(emails); // [a@gmail.com, b@gmail.com]
```

---

📌 En entrevista, lo importante es que puedas responder:

* **ArrayList** = lista ordenada con índice.
* **HashMap** = clave → valor, rápido acceso.
* **HashSet** = conjunto sin duplicados.

---

### Explicación rápida

1. Recorremos el array una sola vez.
2. Guardamos dos variables: `mayor` y `segundoMayor`.
3. Cada vez que encontramos un número más grande que el actual `mayor`, actualizamos ambos.
4. Si no es el mayor, pero es más grande que el `segundoMayor` (y distinto de `mayor`), actualizamos `segundoMayor`.

### Código en Java

```java
public class Main {
    public static int segundoMayor(int[] numeros) {
        int mayor = Integer.MIN_VALUE;
        int segundoMayor = Integer.MIN_VALUE;

        for (int num : numeros) {
            if (num > mayor) {
                // actualizamos ambos
                segundoMayor = mayor;
                mayor = num;
            } else if (num > segundoMayor && num != mayor) {
                // actualizamos solo el segundo
                segundoMayor = num;
            }
        }

        // si no se encontró un segundo mayor válido
        if (segundoMayor == Integer.MIN_VALUE) {
            throw new IllegalArgumentException("No existe un segundo mayor en el arreglo.");
        }

        return segundoMayor;
    }

    public static void main(String[] args) {
        int[] array = {5, 7, 2, 9, 4, 9};
        System.out.println("El segundo mayor es: " + segundoMayor(array));
    }
}
```

### Ejemplo de salida

Si el arreglo es:

```
[5, 7, 2, 9, 4, 9]
```

El mayor es `9`, y el segundo mayor es `7`.
El programa imprimiría:

```
El segundo mayor es: 7
```

---

## `public`

Como ya dijiste, indica que el método es **visible desde cualquier clase**.

* Si fuera `private`, solo se podría usar dentro de la misma clase.
* Si fuera `protected`, desde la clase y sus hijas.
* Si no ponemos nada (default), se puede usar desde clases del mismo *package*.

Eso lo tenés clarísimo 👌.

---

## `static`

Esto significa que el método **pertenece a la clase** y no a un objeto (instancia).
👉 En otras palabras: **no hace falta crear un objeto para llamarlo**.

Ejemplo:

```java
public class Prueba {

    // Método estático
    public static void saludoEstatico() {
        System.out.println("Hola desde static");
    }

    // Método normal (no estático)
    public void saludoNormal() {
        System.out.println("Hola desde objeto");
    }

    public static void main(String[] args) {
        // Llamo al método static directamente con el nombre de la clase
        Prueba.saludoEstatico();

        // Para el otro, necesito crear un objeto
        Prueba p = new Prueba();
        p.saludoNormal();
    }
}
```

### Salida:

```
Hola desde static
Hola desde objeto
```

---

## ¿Por qué en el ejemplo de `segundoMayor` usé `static`?

Porque lo llamamos desde el `main`, que también es `static`.

* En Java, **un método static solo puede llamar a otro static directamente**.
* Si no lo pusiera `static`, tendría que crear un objeto de la clase para usarlo:

```java
public static void main(String[] args) {
    SegundoMayor sm = new SegundoMayor(); // creo objeto
    System.out.println(sm.segundoMayor(new int[]{5, 7, 9}));
}
```

Con `static` me evito esa instancia, y queda más simple para ejemplos.

---

📌 **Regla general** (simplificada):

* Usá `static` si la función **no depende del estado de un objeto** (es decir, solo usa parámetros o variables locales).
* Usá métodos normales (sin static) si la función necesita trabajar con los **atributos del objeto**.

---


