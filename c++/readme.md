Perfecto 👍
Vamos a hacer un **repaso completo de C++ desde cero**, avanzando tema por tema con **teoría clara + ejemplo sencillo** en cada paso.

---

## 🧩 Módulo 1: Introducción a C++

### 🧠 Conceptos teóricos

C++ es un **lenguaje de programación de propósito general**, orientado a objetos y de alto rendimiento.
Se utiliza mucho en **sistemas embebidos, videojuegos, controladores, simulaciones, y aplicaciones de tiempo real**.

Viene de C, pero agrega muchas mejoras:

* **Programación orientada a objetos (POO)** → clases, herencia, polimorfismo, etc.
* **Manejo de memoria más seguro** (con constructores, destructores, referencias, etc.)
* **Bibliotecas estándar (STL)** → `vector`, `string`, `map`, etc.

Un programa en C++ siempre empieza ejecutando la función:

```cpp
int main() {
    // código
    return 0;
}
```

El compilador de C++ más común es **g++** (GNU C++ Compiler).
Para compilar:

```bash
g++ hola.cpp -o hola
./hola
```

---

### 💻 Ejemplo 1: Hola Mundo

```cpp
#include <iostream>  // Librería para entrada/salida estándar

using namespace std;  // Para no escribir std:: cada vez

int main() {
    cout << "Hola, mundo!" << endl;  // Imprime en pantalla
    return 0;
}
```

**Explicación:**

* `#include <iostream>` → incluye funciones de entrada/salida.
* `using namespace std;` → permite usar `cout` y `endl` sin prefijo `std::`.
* `cout` → salida estándar (“console output”).
* `endl` → fin de línea.
* `return 0;` → indica que el programa terminó correctamente.

---

### 🧩 Ejercicio para vos

1. Crea un archivo `hola.cpp`.
2. Copia el código anterior.
3. Compílalo con:

   ```bash
   g++ hola.cpp -o hola
   ./hola
   ```
4. Cambiá el texto a algo como:

   ```cpp
   cout << "Hola Facundo, aprendiendo C++ desde cero!" << endl;
   ```

---

## 🧩 Prefijo `std::` en C++

### 🧠 Teoría

En C++, la librería estándar está dentro del **namespace `std`** (abreviatura de *standard*).
Un *namespace* es un “espacio de nombres” que agrupa funciones, clases y variables para evitar conflictos de nombres.

Cuando escribís:

```cpp
using namespace std;
```

le estás diciendo al compilador:

> “No hace falta que escriba `std::` antes de los nombres de la librería estándar.”

Pero si **no usás** esa línea, tenés que **especificar el espacio de nombres manualmente**, con el prefijo `std::`.

---

### 💻 Ejemplo sin `using namespace std`

```cpp
#include <iostream>

int main() {
    std::cout << "Hola, mundo sin using namespace std!" << std::endl;
    return 0;
}
```

**Explicación:**

* `std::cout` → flujo de salida dentro del namespace `std`.
* `std::endl` → salto de línea dentro del namespace `std`.

Ambas cosas están definidas en la biblioteca `<iostream>`, pero dentro del espacio `std`.

> 🟢 **Buena práctica:**
> En proyectos grandes o profesionales, se recomienda **no usar** `using namespace std;` para evitar conflictos de nombres.
> En programas pequeños o didácticos, sí se puede usar para simplificar.

---

## 🧩 Módulo 2: Variables y tipos de datos básicos

### 🧠 Teoría

Las **variables** son espacios en memoria donde guardamos datos con un tipo específico.
En C++, todos los datos tienen un **tipo definido** (es un lenguaje fuertemente tipado).

| Tipo     | Descripción                           | Ejemplo de valor |
| -------- | ------------------------------------- | ---------------- |
| `int`    | Entero                                | `10`             |
| `float`  | Decimal simple precisión              | `3.14`           |
| `double` | Decimal doble precisión               | `3.141592`       |
| `char`   | Carácter único                        | `'A'`            |
| `string` | Cadena de texto (necesita `<string>`) | `"Hola"`         |
| `bool`   | Verdadero/Falso                       | `true` / `false` |

---

### 💻 Ejemplo 2: Variables y entrada/salida

```cpp
#include <iostream>
#include <string>

int main() {
    int edad;
    std::string nombre;
    double altura;

    std::cout << "Ingresa tu nombre: ";
    std::cin >> nombre;   // lee una palabra (sin espacios)
    
    std::cout << "Ingresa tu edad: ";
    std::cin >> edad;
    
    std::cout << "Ingresa tu altura (en metros): ";
    std::cin >> altura;

    std::cout << "\nHola " << nombre << ", tienes " << edad
              << " años y mides " << altura << " metros." << std::endl;

    return 0;
}
```

---

### 🧠 Notas importantes

* `cin` → lee desde la entrada estándar (teclado).
* `>>` → operador de extracción (obtiene datos del flujo).
* `cout` → operador de inserción (envía datos al flujo de salida).
* Si querés leer frases con espacios (por ejemplo, “Juan Pérez”), debés usar:

  ```cpp
  std::getline(std::cin, nombre);
  ```

---

### 💪 Ejercicio para practicar

Modificá el programa para:

1. Pedir el **nombre completo** del usuario (usando `getline`).
2. Calcular el **año de nacimiento** suponiendo el año actual (por ejemplo, 2025).
3. Mostrar un mensaje como:

   ```
   Hola Juan Pérez, naciste en 1997.
   ```

---

## 🧩 ¿Por qué `std::string` y no `std::int`?

### 🧠 Tipos primitivos vs tipos definidos en la biblioteca estándar

En C++ existen **dos tipos de datos**:

1. **Tipos primitivos** → vienen del lenguaje base (de C).
   Están *“integrados”* en el compilador, no pertenecen a ningún namespace.
   Ejemplos:

   ```cpp
   int, float, double, char, bool
   ```

   👉 Por eso **no llevan `std::`**, porque no están dentro del espacio de nombres `std`.

2. **Tipos definidos en la biblioteca estándar (STL)** → son clases y estructuras que *sí* están en el namespace `std`.
   Ejemplos:

   ```cpp
   std::string, std::vector, std::map, std::cout, std::cin
   ```

   👉 Por eso **sí llevan `std::`**: porque están definidos dentro del espacio `std`.

---

### 💡 Ejemplo comparativo

```cpp
#include <iostream>
#include <string>

int main() {
    int edad = 30;                  // tipo primitivo → sin std::
    double altura = 1.80;           // tipo primitivo
    std::string nombre = "Facundo"; // tipo de la STL → con std::

    std::cout << "Nombre: " << nombre << std::endl;
    std::cout << "Edad: " << edad << ", Altura: " << altura << " m" << std::endl;

    return 0;
}
```

> 🔹 `int` y `double` → no necesitan `std::`
> 🔹 `std::string` → sí, porque está definido dentro del espacio `std`
> 🔹 `std::cout` y `std::endl` → también están dentro de `std`

---

## 🧩 Módulo 3: Operadores y estructuras condicionales

### 🧠 Teoría

Los **operadores** y **estructuras condicionales** permiten tomar decisiones y realizar cálculos.

---

### ⚙️ Operadores básicos

| Tipo        | Ejemplo                          | Descripción                                   |        |              |
| ----------- | -------------------------------- | --------------------------------------------- | ------ | ------------ |
| Aritméticos | `+`, `-`, `*`, `/`, `%`          | Suma, resta, multiplicación, división, módulo |        |              |
| Comparación | `==`, `!=`, `<`, `>`, `<=`, `>=` | Comparan valores y devuelven `true` o `false` |        |              |
| Lógicos     | `&&`, `                          |                                               | `, `!` | AND, OR, NOT |
| Asignación  | `=`, `+=`, `-=`, `*=`, `/=`      | Asignar o modificar valores                   |        |              |

---

### 🧩 Estructuras condicionales

#### `if` / `else if` / `else`

Permiten ejecutar bloques de código según una condición.

```cpp
#include <iostream>

int main() {
    int numero;

    std::cout << "Ingresa un número: ";
    std::cin >> numero;

    if (numero > 0) {
        std::cout << "El número es positivo." << std::endl;
    } else if (numero < 0) {
        std::cout << "El número es negativo." << std::endl;
    } else {
        std::cout << "El número es cero." << std::endl;
    }

    return 0;
}
```

---

#### `switch`

Se usa cuando hay muchas comparaciones sobre una misma variable.

```cpp
#include <iostream>

int main() {
    int opcion;

    std::cout << "Menú principal:" << std::endl;
    std::cout << "1. Encender" << std::endl;
    std::cout << "2. Apagar" << std::endl;
    std::cout << "3. Reiniciar" << std::endl;
    std::cout << "Elige una opción: ";
    std::cin >> opcion;

    switch (opcion) {
        case 1:
            std::cout << "Sistema encendido." << std::endl;
            break;
        case 2:
            std::cout << "Sistema apagado." << std::endl;
            break;
        case 3:
            std::cout << "Reiniciando sistema..." << std::endl;
            break;
        default:
            std::cout << "Opción no válida." << std::endl;
            break;
    }

    return 0;
}
```

**Explicación:**

* `switch` evalúa `opcion`.
* Cada `case` es un valor posible.
* `break` evita que se ejecuten los siguientes casos.
* `default` se ejecuta si ninguno coincide.

---

### 💪 Ejercicio práctico

Crea un programa que:

1. Pida al usuario dos números enteros.
2. Pregunte qué operación quiere realizar: `+`, `-`, `*`, `/`.
3. Use `switch` para ejecutar la operación y mostrar el resultado.
   Ejemplo:

   ```
   Ingresa primer número: 6
   Ingresa segundo número: 3
   Operación (+, -, *, /): *
   Resultado: 18
   ```

---

## 🧩 Módulo 4: Bucles o estructuras repetitivas

### 🧠 Teoría general

Los **bucles** permiten repetir un bloque de código varias veces.
Son esenciales para tareas como recorrer listas, leer sensores, calcular promedios, etc.

Los tres principales en C++ son:

1. `for` → cuando sabés cuántas veces vas a repetir algo.
2. `while` → cuando repetís mientras una condición sea verdadera.
3. `do while` → igual que `while`, pero se ejecuta al menos una vez.

---

## 🔹 1. Bucle `for`

### 💡 Estructura general

```cpp
for (inicialización; condición; incremento) {
    // código a repetir
}
```

### 💻 Ejemplo

```cpp
#include <iostream>

int main() {
    std::cout << "Contador ascendente:" << std::endl;

    for (int i = 1; i <= 5; i++) {
        std::cout << "Iteración " << i << std::endl;
    }

    return 0;
}
```

**Explicación:**

* `int i = 1` → valor inicial.
* `i <= 5` → condición de repetición.
* `i++` → se ejecuta al final de cada ciclo (incrementa `i` en 1).

👉 El bucle se ejecuta **mientras la condición sea verdadera**.

---

## 🔹 2. Bucle `while`

### 💡 Estructura general

```cpp
while (condición) {
    // código a repetir
}
```

### 💻 Ejemplo

```cpp
#include <iostream>

int main() {
    int contador = 0;

    std::cout << "Contador con while:" << std::endl;

    while (contador < 3) {
        std::cout << "Valor: " << contador << std::endl;
        contador++; // importante incrementar, si no queda en bucle infinito
    }

    return 0;
}
```

---

## 🔹 3. Bucle `do while`

### 💡 Estructura general

```cpp
do {
    // código a repetir
} while (condición);
```

### 💻 Ejemplo

```cpp
#include <iostream>

int main() {
    int numero;

    do {
        std::cout << "Ingresa un número positivo: ";
        std::cin >> numero;
    } while (numero < 0);

    std::cout << "Número válido: " << numero << std::endl;

    return 0;
}
```

**Explicación:**

* El `do` ejecuta **al menos una vez**, incluso si la condición es falsa al inicio.
* Ideal cuando querés validar datos de entrada del usuario.

---

## 🔹 Palabras clave útiles

| Palabra    | Función                                                   |
| ---------- | --------------------------------------------------------- |
| `break`    | Sale del bucle antes de tiempo                            |
| `continue` | Salta al siguiente ciclo sin ejecutar el resto del bloque |

### 💻 Ejemplo

```cpp
#include <iostream>

int main() {
    for (int i = 1; i <= 5; i++) {
        if (i == 3) {
            std::cout << "Salteando el número 3" << std::endl;
            continue; // salta al siguiente ciclo
        }
        if (i == 5) {
            std::cout << "Saliendo del bucle en i = " << i << std::endl;
            break; // termina el bucle completamente
        }
        std::cout << "Valor actual: " << i << std::endl;
    }

    return 0;
}
```

---

## 💪 Ejercicio para vos

1. Escribí un programa que pida un número `n` y muestre la **tabla de multiplicar** del 1 al 10 usando un bucle `for`.
   Ejemplo:

   ```
   Ingresa un número: 4
   4 x 1 = 4
   4 x 2 = 8
   ...
   4 x 10 = 40
   ```

2. Modificá el mismo programa para que, si el usuario ingresa un número negativo, le vuelva a pedir otro número (usando `do while`).

---

