
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

