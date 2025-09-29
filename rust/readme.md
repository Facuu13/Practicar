
---

## 1. ¿Qué es Rust?

* **Lenguaje compilado y moderno**, creado por Mozilla.
* **Seguro en memoria**: evita errores típicos de C/C++ (punteros inválidos, uso después de liberar memoria).
* **Rápido como C/C++**, pero con la facilidad de alto nivel de Python.
* Usa un sistema de **propiedad (ownership)** y **préstamos (borrowing)** en lugar de un garbage collector.

---

## 2. Hola Mundo

Siempre se empieza así 😅:

```rust
fn main() {
    println!("Hola, Rust!");
}
```

👉 `fn` define una función, `main` es el punto de entrada, y `println!` (con `!`) es una macro que imprime en pantalla.

---

## 3. Variables

* Por defecto, **las variables son inmutables** (`let`).
* Si quieres que se puedan cambiar, usas `mut`.

```rust
fn main() {
    let x = 5;      // inmutable
    let mut y = 10; // mutable

    println!("x = {}, y = {}", x, y);

    y = 20; // OK porque y es mutable
    println!("nuevo y = {}", y);
}
```

---

## 4. Tipos de datos básicos

Rust es fuertemente tipado:

* Enteros: `i32`, `u32`, `i64`…
* Flotantes: `f32`, `f64`
* Booleanos: `bool`
* Texto: `&str` (string inmutable), `String` (string dinámico)

```rust
fn main() {
    let entero: i32 = 42;
    let decimal: f64 = 3.14;
    let verdad: bool = true;
    let saludo: &str = "Hola";
    let nombre: String = String::from("Facu");

    println!("{} {} {}", entero, decimal, nombre);
}
```

---

## 5. Condicionales

Muy similar a otros lenguajes, pero sin paréntesis obligatorios.

```rust
fn main() {
    let edad = 20;

    if edad >= 18 {
        println!("Eres mayor de edad");
    } else {
        println!("Eres menor de edad");
    }
}
```

---

## 6. Bucles

Rust tiene:

* `loop` → bucle infinito
* `while` → mientras condición
* `for` → iteración sobre rangos o colecciones

```rust
fn main() {
    // loop infinito con break
    let mut n = 0;
    loop {
        n += 1;
        if n == 3 {
            break;
        }
        println!("n = {}", n);
    }

    // while
    let mut m = 0;
    while m < 3 {
        println!("m = {}", m);
        m += 1;
    }

    // for con rango
    for i in 0..3 {
        println!("i = {}", i);
    }
}
```

---

## 7. Funciones

```rust
fn suma(a: i32, b: i32) -> i32 {
    a + b  // la última expresión es el retorno (sin ;)
}

fn main() {
    let r = suma(3, 4);
    println!("Resultado = {}", r);
}
```

---

## 8. Vectores y colecciones

Un **vector** es como un array dinámico.

```rust
fn main() {
    let mut numeros = vec![1, 2, 3]; // vec! es una macro
    numeros.push(4);

    for n in &numeros {
        println!("{}", n);
    }
}
```

---

Perfecto 🙌, vamos a profundizar en **colecciones en Rust**, porque son súper importantes y se usan en casi todos los programas.

En Rust, las colecciones más comunes son:

1. **Vectores (`Vec<T>`)** → listas dinámicas.
2. **Strings (`String`)** → cadenas de texto mutables.
3. **HashMap<K, V>** → pares clave-valor (como un diccionario en Python).

---

## 1. Vectores (`Vec<T>`)

Son arrays que pueden crecer o achicarse. Se definen con `vec![]`.

```rust
fn main() {
    let mut numeros = vec![10, 20, 30];  // vector con valores iniciales
    numeros.push(40);                     // agregar un valor
    numeros.remove(1);                    // elimina el valor en índice 1 (20)

    println!("{:?}", numeros); // {:?} muestra el vector completo
}
```

👉 Métodos útiles:

* `.push(x)` → agrega al final
* `.pop()` → saca el último elemento
* `.len()` → devuelve la longitud
* `.iter()` → itera sin consumir
* `.contains(&x)` → pregunta si existe un valor

Ejemplo con iteración:

```rust
fn main() {
    let numeros = vec![1, 2, 3, 4, 5];

    for n in &numeros {
        println!("Número: {}", n);
    }

    println!("El vector tiene {} elementos", numeros.len());
}
```

---

## 2. Strings

En Rust hay dos formas de manejar texto:

* `&str` → slice inmutable (literal como `"hola"`).
* `String` → cadena dinámica, mutable.

```rust
fn main() {
    let mut saludo = String::from("Hola");
    saludo.push_str(", Facu!"); // agrega texto

    println!("{}", saludo);

    // Slicing: obtener parte del string
    let hola = &saludo[0..4];
    println!("{}", hola);
}
```

👉 Métodos útiles:

* `.push_str("texto")` → agrega texto
* `.len()` → longitud en bytes
* `.replace("a", "x")` → reemplazo
* `.split_whitespace()` → separar por espacios

```rust
fn main() {
    let frase = String::from("Rust es poderoso y seguro");

    for palabra in frase.split_whitespace() {
        println!("Palabra: {}", palabra);
    }
}
```

---

## 3. HashMap (clave → valor)

Similar a un diccionario en Python o `map` en Java.

```rust
use std::collections::HashMap;

fn main() {
    let mut edades = HashMap::new();

    edades.insert("Alice", 25);
    edades.insert("Bob", 30);

    println!("{:?}", edades);

    // obtener un valor
    if let Some(edad) = edades.get("Alice") {
        println!("La edad de Alice es {}", edad);
    }

    // iterar sobre pares
    for (nombre, edad) in &edades {
        println!("{} tiene {} años", nombre, edad);
    }
}
```

👉 Métodos útiles:

* `.insert(clave, valor)` → agrega o actualiza
* `.get(&clave)` → devuelve `Option<&valor>`
* `.remove(&clave)` → elimina
* `.contains_key(&clave)` → pregunta si existe

---

✅ Resumen rápido:

* **Vec** → listas ordenadas, indexadas por número.
* **String** → texto mutable, más poderoso que `&str`.
* **HashMap** → pares clave-valor, no ordenados.

---

# 🔑 Concepto 1: Ownership (propiedad)

En Rust, **cada valor en memoria tiene un único dueño**.
Cuando el dueño sale de alcance, el valor se libera automáticamente.

Ejemplo:

```rust
fn main() {
    let s1 = String::from("Hola"); // s1 es el dueño del String
    let s2 = s1;                   // propiedad se transfiere a s2

    // println!("{}", s1);  ❌ ERROR: s1 ya no es dueño
    println!("{}", s2);  // ✅ funciona
}
```

👉 Cuando haces `let s2 = s1;`, el ownership pasa de `s1` a `s2`.
Rust hace esto para evitar **doble liberación de memoria**.

---

# 🔑 Concepto 2: Borrowing (préstamo)

Si quieres usar una variable sin perder la propiedad, puedes **prestarla como referencia** usando `&`.

```rust
fn main() {
    let s1 = String::from("Hola");
    let len = calcular_longitud(&s1); // paso referencia
    println!("'{}' tiene longitud {}", s1, len);
}

fn calcular_longitud(s: &String) -> usize {
    s.len() // uso la referencia sin tomar la propiedad
}
```

👉 `&s1` significa "préstamo".
El dueño sigue siendo `s1`, pero la función lo puede leer.

---

# 🔑 Concepto 3: Mutable Borrowing

Si quieres modificar un valor prestado, usas `&mut`.
⚠️ Regla: solo puede haber **un préstamo mutable a la vez** (para evitar condiciones de carrera).

```rust
fn main() {
    let mut s = String::from("Hola");
    cambiar(&mut s);
    println!("{}", s);
}

fn cambiar(texto: &mut String) {
    texto.push_str(", mundo!");
}
```

👉 Así, se modifica `s` sin transferir la propiedad.

---

# 🔑 Concepto 4: Diferencia entre Copy y Move

Algunos tipos simples (`i32`, `bool`, `f64`) se copian automáticamente porque son livianos.

```rust
fn main() {
    let x = 5;
    let y = x; // se copia, no se mueve

    println!("x = {}, y = {}", x, y); // ambos siguen válidos
}
```

👉 Tipos simples implementan el *trait* `Copy`.
En cambio, `String` o `Vec` son pesados y se mueven por defecto.

---

# ⚡ Mini-ejemplo integrador

```rust
fn main() {
    let mut numeros = vec![1, 2, 3];

    // préstamo inmutable
    imprimir(&numeros);

    // préstamo mutable
    agregar(&mut numeros);

    println!("Final: {:?}", numeros);
}

fn imprimir(v: &Vec<i32>) {
    println!("Vector: {:?}", v);
}

fn agregar(v: &mut Vec<i32>) {
    v.push(4);
}
```

👉 Resultado:

```
Vector: [1, 2, 3]
Final: [1, 2, 3, 4]
```

---

✅ Resumen:

* Cada valor tiene **un dueño**.
* Cuando el dueño muere, el valor se libera.
* Se puede **prestar** con `&` (lectura) o `&mut` (modificación).
* Tipos simples (`i32`, `bool`) se **copian**, no se mueven.

---


¡De una! Vamos a **iterar colecciones en Rust** con `iter`, `iter_mut` e `into_iter`, paso a paso, con mini-ejemplos claros.

---

# 1) ¿Qué es un iterador?

Un **iterador** es un objeto que produce ítems uno a uno cuando llamás a `next()`.
En Rust, casi nunca llamás `next()` a mano: usás `for`, o métodos como `find`, `map`, `filter`, etc.

* `v.iter()` → itera por **referencias inmutables**: `&T`
* `v.iter_mut()` → itera por **referencias mutables**: `&mut T`
* `v.into_iter()` → **consume** la colección y produce **valores**: `T`

> Azúcar sintáctico de `for`:
>
> * `for x in v` usa `into_iter()` (consume `v`)
> * `for x in &v` usa `iter()`
> * `for x in &mut v` usa `iter_mut()`

---

# 2) Leer elementos (iteración inmutable)

```rust
fn main() {
    let numeros = vec![10, 20, 30];

    // Formas equivalentes
    for n in &numeros {           // azúcar de numeros.iter()
        println!("n = {}", n);
    }

    numeros.iter().for_each(|n| {
        println!("otra vez: {}", n);
    });

    // El vector sigue disponible (no fue consumido)
    println!("len = {}", numeros.len());
}
```

* `&numeros` / `.iter()` ⇒ te da `&i32` (referencias de solo lectura).

---

# 3) Modificar elementos (iteración mutable)

```rust
fn main() {
    let mut nums = vec![1, 2, 3];

    for n in &mut nums {          // azúcar de nums.iter_mut()
        *n += 10;                 // desreferencia para escribir
    }

    println!("{:?}", nums);       // [11, 12, 13]
}
```

* `&mut nums` / `.iter_mut()` ⇒ te da `&mut i32` para poder **cambiar**.

---

# 4) Consumir la colección (into_iter)

```rust
fn main() {
    let nums = vec![1, 2, 3];

    // into_iter mueve (consume) cada elemento
    let textos: Vec<String> = nums
        .into_iter()
        .map(|n| format!("n={}", n)) // acá ya tenés valores, no referencias
        .collect();

    println!("{:?}", textos);
    // ¡Ojo! nums ya no existe aquí (fue consumido).
}
```

Usá `into_iter` cuando necesitás **tomar ownership** de los ítems o **convertir** la colección.

---

# 5) Buscar elementos

### `find` (devuelve Option<&T> o Option<T> según el iterador)

```rust
fn main() {
    let nums = vec![10, 20, 30];

    if let Some(x) = nums.iter().find(|&&n| n > 15) {
        println!("encontré: {}", x);   // x: &i32
    }

    // posición (índice)
    if let Some(i) = nums.iter().position(|&n| n == 20) {
        println!("índice de 20: {}", i);
    }
}
```

> Nota: con `iter()` el cierre recibe `&&i32` si usás `|n|`; una forma común es `|&n|` para “copiar” a `n`.

---

# 6) Predicados útiles: `any`, `all`, `contains`

```rust
fn main() {
    let nums = vec![1, 2, 3, 4];

    let hay_par = nums.iter().any(|&n| n % 2 == 0);
    let todos_positivos = nums.iter().all(|&n| n > 0);
    let tiene_tres = nums.contains(&3); // método de Vec, usa PartialEq

    println!("{hay_par} {todos_positivos} {tiene_tres}");
}
```

---

# 7) `enumerate` (índice + valor)

```rust
fn main() {
    let v = vec!["temp", "hum", "luz"];

    for (i, nombre) in v.iter().enumerate() {
        println!("#{i} -> {nombre}");
    }
}
```

---

# 8) `map` y `filter` (+ `collect`)

```rust
fn main() {
    let nums = vec![1, 2, 3, 4, 5];

    let cuadrados: Vec<i32> = nums.iter().map(|&n| n * n).collect();
    let pares: Vec<i32>      = nums.iter().copied().filter(|n| n % 2 == 0).collect();

    println!("{:?} {:?}", cuadrados, pares);
}
```

* `copied()` transforma `&i32` → `i32` (copia) para evitar `|&n|`.

---

# 9) Slices y arrays también “iteran”

```rust
fn main() {
    let arr = [10, 20, 30];
    for x in arr.iter() {
        println!("{}", x);
    }

    let slice: &[i32] = &arr[0..2];
    for x in slice {
        println!("slice: {}", x);
    }
}
```

---

# 10) Iterar structs (ejemplo IoT rápido)

```rust
struct Sensor { nombre: String, valor: i32 }

fn main() {
    let mut sensores = vec![
        Sensor { nombre: "Temp".into(),   valor: 22 },
        Sensor { nombre: "Humedad".into(), valor: 60 },
    ];

    // Leer
    for s in &sensores {
        println!("{} = {}", s.nombre, s.valor);
    }

    // Modificar (sumar 1 a todas las lecturas)
    for s in &mut sensores {
        s.valor += 1;
    }
}
```

---

## Errores comunes (y cómo evitarlos)

* **Consumir sin querer**: `for x in v { ... }` consume `v`. Si después querés usar `v`, iterá con `&v` o `&mut v`.
* **Mezclar préstamos**: no podés tener a la vez un préstamo mutable y otro inmutable sobre el **mismo** dato/colección.
* **Mover valores al cerrar**: si usás `into_iter()` en un `Vec<String>`, cada `String` se mueve. Usá `iter()` si solo leés.

---

## Mini-prácticas (sin código, para que pruebes vos)

1. Dado `Vec<i32>`, imprimí solo los impares usando `iter().filter(...)`.
2. Dado `Vec<String>`, creá un nuevo `Vec<usize>` con las longitudes (`map` + `collect`).
3. En `Vec<Sensor>`, buscá el índice del sensor `"Temp"` con `position` y actualizá su `valor` sumando 5 (pista: `&mut [Sensor]`).
4. Usá `enumerate` para imprimir `#idx: nombre=valor` de todos los sensores.
5. Verificá con `any` si **algún** sensor supera `100`, y con `all` si **todos** son mayores a `0`.

---




