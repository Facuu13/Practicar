
---

# 🟢 Ejercicio IoT 1 (Rust, Struct + Funciones)

**Monitoreo de un sensor de temperatura 🌡️**

### Requisitos

1. Crear un `struct Sensor`:

   * Atributos:

     * `nombre` (String)
     * `valor` (i32)

2. Crear funciones:

   * `crear_sensor(nombre: &str, valor: i32) -> Sensor`
     👉 Devuelve un sensor nuevo.
   * `mostrar(sensor: &Sensor)`
     👉 Muestra en consola: `"Sensor Temp = 25°C"`.
   * `actualizar(sensor: &mut Sensor, nuevo_valor: i32)`
     👉 Cambia el valor del sensor.

3. En el programa principal (`main`):

   * Crear un sensor de temperatura con valor inicial 22.
   * Mostrar el sensor.
   * Actualizar su valor a 28.
   * Mostrarlo de nuevo.

---

⚡ Este problema es sencillo, pero ya vas a practicar:

* **Structs** (modelar objetos IoT).
* **Ownership y borrowing** (`&` y `&mut`).
* **Funciones** que leen y modifican.

---
```rust
struct Sensor {
    nombre: String,
    valor: i32,
}

fn crear_sensor(nombre: &str, valor: i32) -> Sensor{

   let s = Sensor { nombre: String::from(nombre), valor: valor};
    return s
    
}

fn mostrar(sensor: &Sensor){
    println!("Sensor {} = {}°C", sensor.nombre, sensor.valor);
    
}

fn actualizar(sensor: &mut Sensor, nuevo_valor: i32){
    sensor.valor = nuevo_valor;
}

fn main() {
    let mut s=crear_sensor("temp",25);
    mostrar(&s);
    actualizar(&mut s,45);
    mostrar(&s);
}
```