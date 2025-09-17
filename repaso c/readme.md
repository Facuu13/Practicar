Perfecto, arranquemos con **punteros en C** 👇

---

## 📌 Concepto de punteros

En C, un puntero es una **variable que guarda la dirección de memoria** de otra variable.
En lugar de guardar un valor directo (ej: un `int` con el valor `10`), guarda la “dirección” en la memoria donde está ese valor.

👉 Esto es útil para:

* Acceder y modificar variables indirectamente.
* Pasar grandes estructuras a funciones sin copiarlas enteras.
* Trabajar con arreglos y strings.
* Manejo de memoria dinámica (`malloc`, `free`, etc.).

Se usan dos operadores principales:

* `&` → obtiene la dirección de memoria de una variable.
* `*` → accede al valor almacenado en la dirección que apunta el puntero (se llama *desreferenciar*).

---

## 📌 Ejemplo sencillo

```c
#include <stdio.h>

int main() {
    int numero = 42;         // una variable normal
    int *ptr;                // declaración de un puntero a int

    ptr = &numero;           // el puntero guarda la dirección de 'numero'

    printf("Valor de numero: %d\n", numero);
    printf("Direccion de numero: %p\n", &numero);
    printf("Direccion guardada en ptr: %p\n", ptr);
    printf("Valor al que apunta ptr: %d\n", *ptr); // desreferencia -> obtiene 42

    // Ahora modificamos el valor usando el puntero
    *ptr = 100;
    printf("Nuevo valor de numero: %d\n", numero);

    return 0;
}
```

### 🔎 Explicación rápida

1. `int *ptr;` → declaro un puntero a entero.
2. `ptr = &numero;` → guardo la dirección de `numero`.
3. `*ptr` → accedo al valor que está en esa dirección.
4. Si modifico `*ptr`, en realidad estoy modificando a `numero`.

---


## 📌 Concepto: punteros y arreglos

En C, el **nombre de un arreglo** se comporta como un **puntero al primer elemento**.
Eso significa que:

* `arreglo[i]` es lo mismo que `*(arreglo + i)`.
* Los punteros permiten recorrer arreglos sin necesidad de usar índices.
* Se puede pasar un arreglo a una función como si fuera un puntero.

---

## 📌 Ejemplo sencillo

```c
#include <stdio.h>

int main() {
    int numeros[5] = {10, 20, 30, 40, 50};

    // Un puntero que apunta al primer elemento
    int *ptr = numeros;

    // Imprimir usando índices normales
    printf("Usando indices:\n");
    for (int i = 0; i < 5; i++) {
        printf("numeros[%d] = %d\n", i, numeros[i]);
    }

    // Imprimir usando punteros
    printf("\nUsando punteros:\n");
    for (int i = 0; i < 5; i++) {
        printf("*(ptr + %d) = %d\n", i, *(ptr + i));
    }

    return 0;
}
```

---

### 🔎 Explicación rápida

1. `numeros` es un arreglo, pero también se puede usar como puntero a `&numeros[0]`.
2. `ptr = numeros;` → el puntero guarda la dirección del primer elemento.
3. `*(ptr + i)` → accede al valor del índice `i`.

   * `*(ptr + 0)` → `10`
   * `*(ptr + 1)` → `20`
   * etc.

---

👉 Esto es clave para entender cómo se manejan los **strings en C** (que son básicamente arreglos de `char` + un `'\0'` al final).


---

## 📌 Concepto

En C, las funciones **reciben los argumentos por valor**, es decir, se hace una copia.
Si querés que una función **modifique la variable original**, no alcanza con pasarla así nomás: tenés que pasar un **puntero a esa variable** (su dirección de memoria).

Esto se llama **paso por referencia**.

---

## 📌 Ejemplo sencillo

```c
#include <stdio.h>

// Función que recibe un puntero a int
void duplicar(int *x) {
    *x = *x * 2;   // modifico el valor que está en la dirección
}

int main() {
    int numero = 10;

    printf("Antes de llamar a la funcion: %d\n", numero);

    duplicar(&numero);  // paso la dirección de numero

    printf("Despues de llamar a la funcion: %d\n", numero);

    return 0;
}
```

---

### 🔎 Explicación rápida

1. `void duplicar(int *x)` → la función espera un puntero a un entero.
2. `duplicar(&numero)` → le paso la **dirección** de `numero`.
3. Dentro de la función, `*x` accede al valor original, no a una copia.
4. Cuando modifico `*x`, realmente estoy cambiando `numero` en `main`.

---

👉 Este concepto es el que se usa mucho para:

* **Funciones que devuelven múltiples valores.**
* **Trabajar con arreglos en funciones.**
* **Manejo de memoria dinámica (`malloc`)**.

---


## 📌 Concepto: punteros y strings

En C, un **string no es un tipo de dato especial**, sino un **arreglo de caracteres** terminado en `'\0'` (carácter nulo).

Ejemplo:

```c
char saludo[] = "Hola";
```

En memoria es:

```
'H'  'o'  'l'  'a'  '\0'
```

El nombre del arreglo (`saludo`) se comporta como un **puntero al primer carácter**.
Por eso, se puede recorrer el string con índices o con punteros.

---

## 📌 Ejemplo sencillo

```c
#include <stdio.h>

int main() {
    char saludo[] = "Hola";

    // Usando indices
    printf("Usando indices:\n");
    for (int i = 0; saludo[i] != '\0'; i++) {
        printf("saludo[%d] = %c\n", i, saludo[i]);
    }

    // Usando puntero
    printf("\nUsando punteros:\n");
    char *ptr = saludo; // apunta al primer caracter
    while (*ptr != '\0') {
        printf("%c\n", *ptr);
        ptr++; // avanzar al siguiente caracter
    }

    return 0;
}
```

---

### 🔎 Explicación rápida

1. `char saludo[] = "Hola";` → crea un arreglo de 5 caracteres (`H`, `o`, `l`, `a`, `\0`).
2. `char *ptr = saludo;` → el puntero apunta al primer carácter.
3. `*ptr` → accede al carácter actual.
4. `ptr++` → avanza al siguiente carácter en memoria.
5. El loop termina al encontrar el `'\0'`.

---

👉 Este mecanismo se usa en funciones estándar como:

* `strlen()` → cuenta caracteres hasta `'\0'`.
* `strcpy()` → copia strings carácter por carácter usando punteros.
* `printf("%s")` → imprime caracteres hasta `'\0'`.

---

## 📌 Concepto: memoria dinámica

En C, las variables normalmente se guardan en **stack** (pila), y su vida depende del **scope** (por ejemplo, al salir de una función se borran).

Pero a veces necesitamos:

* Crear estructuras cuyo tamaño no conocemos en tiempo de compilación.
* Reservar memoria que viva más allá de una función.
* Manejar grandes bloques de datos.

👉 Para eso está la **memoria dinámica** (heap).
Se reserva y libera manualmente usando funciones de la librería `<stdlib.h>`:

* `malloc(tamaño_en_bytes)` → reserva memoria y devuelve un **puntero genérico (`void*`)**.
* `free(puntero)` → libera la memoria reservada.
* `calloc(n, size)` → como `malloc`, pero inicializa en `0`.
* `realloc(ptr, nuevo_tamaño)` → cambia el tamaño de un bloque de memoria.

⚠️ Importante: siempre que uses `malloc`, más tarde tenés que llamar a `free` para evitar **memory leaks**.

---

## 📌 Ejemplo sencillo con `malloc` y `free`

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    printf("Cuantos numeros queres guardar? ");
    scanf("%d", &n);

    // Reservo memoria para n enteros
    int *numeros = (int*) malloc(n * sizeof(int));

    if (numeros == NULL) { // siempre chequear
        printf("Error al reservar memoria\n");
        return 1;
    }

    // Cargo valores
    for (int i = 0; i < n; i++) {
        numeros[i] = i * 10; // uso como si fuera un arreglo normal
    }

    // Muestro valores
    printf("Valores guardados:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", numeros[i]);
    }
    printf("\n");

    // Libero memoria
    free(numeros);

    return 0;
}
```

---

### 🔎 Explicación rápida

1. `malloc(n * sizeof(int))` → reserva memoria suficiente para `n` enteros.

   * Si `n=5`, reserva `5 * 4 = 20 bytes` (en un sistema de 32 bits).
2. `numeros[i]` funciona igual que un arreglo.
3. Siempre hay que verificar que `malloc` no devuelva `NULL`.
4. `free(numeros);` → libera la memoria, muy importante.

---

👉 Esto es fundamental cuando trabajás con:

* Arreglos cuyo tamaño depende de datos de entrada.
* Estructuras como **listas enlazadas, árboles, colas**.
* Programas que necesitan manejar mucha memoria y no pueden depender solo del stack.

---

---

## 📌 Concepto: estructuras

Una **estructura (`struct`)** en C permite agrupar **distintos tipos de datos** bajo un mismo nombre.
Es como un "paquete" de variables relacionadas.

Ejemplo típico: representar un **sensor** con ID, nombre y valor.

```c
struct Sensor {
    int id;
    char nombre[20];
    float valor;
};
```

* `struct Sensor` es un nuevo tipo de dato.
* Cada campo puede ser de distinto tipo (`int`, `char[]`, `float`, etc.).
* Se accede con `.` (punto) cuando es una variable normal.
* Con punteros se accede con `->`.

---

## 📌 Ejemplo sencillo

```c
#include <stdio.h>
#include <string.h>

struct Sensor {
    int id;
    char nombre[20];
    float valor;
};

int main() {
    // Crear una estructura normal
    struct Sensor s1;
    s1.id = 1;
    strcpy(s1.nombre, "Temperatura");
    s1.valor = 23.5;

    printf("Sensor: %d, %s, %.2f\n", s1.id, s1.nombre, s1.valor);

    // Usar un puntero a estructura
    struct Sensor *ptr = &s1;

    // Acceso con flecha (->)
    ptr->valor = 25.0;  
    printf("Nuevo valor: %.2f\n", ptr->valor);

    return 0;
}
```

---

### 🔎 Explicación rápida

1. `struct Sensor s1;` → creo una variable de tipo `Sensor`.
2. `s1.id`, `s1.nombre`, `s1.valor` → accedo con `.` porque es una variable normal.
3. `struct Sensor *ptr = &s1;` → creo un puntero que apunta a la estructura.
4. `ptr->valor` → equivalente a `(*ptr).valor`.

   * La flecha `->` es un atajo para trabajar con punteros a estructuras.

---

👉 Esto es fundamental en C porque:

* Se usan para modelar entidades más complejas (sensores, nodos, clientes, etc.).
* Con punteros + memoria dinámica podés crear **listas, árboles, colas, etc.**
* Es la base de cómo se implementan muchas estructuras de datos en C.

---


# 📌 Concepto de **Cola**

Una **cola (queue)** es como una **fila de personas en un banco o supermercado**:

* El **primero en entrar es el primero en salir** → **FIFO** (*First In, First Out*).
* Tenés dos operaciones principales:

  * **Enqueue** → alguien entra a la fila (se agrega al final).
  * **Dequeue** → atienden al que está primero (se saca del frente).

---

## 📌 Ejemplo muy sencillo en C (cola con arreglo chico)

```c
#include <stdio.h>

#define MAX 3   // tamaño máximo de la cola

int main() {
    int cola[MAX];   // arreglo para guardar los elementos
    int frente = 0;  // índice del primero
    int final = 0;   // índice del último
    int cantidad = 0; // cuántos hay en la cola

    // ENQUEUE: agregamos elementos
    if (cantidad < MAX) { cola[final++] = 10; cantidad++; }
    if (cantidad < MAX) { cola[final++] = 20; cantidad++; }
    if (cantidad < MAX) { cola[final++] = 30; cantidad++; }

    // Mostramos la cola
    printf("Cola actual: ");
    for (int i = frente; i < final; i++) {
        printf("%d ", cola[i]);
    }
    printf("\n");

    // DEQUEUE: sacamos el primero
    if (cantidad > 0) {
        int primero = cola[frente++];
        cantidad--;
        printf("Dequeue: %d\n", primero);
    }

    // Mostramos la cola otra vez
    printf("Cola despues de sacar uno: ");
    for (int i = frente; i < final; i++) {
        printf("%d ", cola[i]);
    }
    printf("\n");

    return 0;
}
```

---

### 🔎 Qué pasa acá

1. Metemos `10`, `20`, `30` en la cola → queda: **10 20 30**.
2. Hacemos un `dequeue` → sale el **10** (el primero que entró).
3. La cola queda: **20 30**.

---

👉 Con este ejemplo mínimo se ve clarito:

* Entran siempre por un lado (**final**).
* Salen siempre por el otro (**frente**).

---

