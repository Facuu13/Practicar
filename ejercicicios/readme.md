
---

### 📌 Ejercicio 1: Número par o impar

Escribí un programa que:

1. Pida un número entero al usuario.
2. Determine si el número es **par** o **impar**.
3. Muestre el resultado por pantalla.

---
#### En C

```c
#include <stdio.h>

int main()
{
    int miNumero;
    printf("Ingrese un numero entero: ");
    scanf("%d", &miNumero);
    if (miNumero%2==0){
        printf("El numero ingresado es par");
    }
    else{
        printf("El numero ingresado es impar ");
    }

    return 0;
}

```
#### En Python

```python
mi_numero_entero = int(input("Ingresa un número entero: "))
if mi_numero_entero %2 == 0:
    print("numero par")
else:
    print("numero impar")
```
#### En Java
```java
import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in); // 2. Crear un objeto Scanner

        System.out.print("Por favor, ingresa un número entero: "); // 3. Solicitar al usuario
        int numeroEntero = scanner.nextInt();
        
        if (numeroEntero%2 == 0){
            System.out.print("Numero Par");
        }
        else{
            System.out.print("Numero Impar");
        }
        
        scanner.close();
	}
}
```


---

### 📌 Ejercicio 2: Suma de números en un arreglo/lista

Escribí un programa que:

1. Pida al usuario cuántos números quiere ingresar.
2. Lea esos números y los guarde en un arreglo (C/Java) o lista (Python).
3. Calcule la **suma total** de los números ingresados.
4. Muestre el resultado por pantalla.

#### En C

```c
#include <stdio.h>

int main() {
    int n, i;
    int suma = 0;

    printf("¿Cuántos números querés ingresar?: ");
    scanf("%d", &n);

    int numeros[n];  // arreglo de tamaño dinámico (C99 en adelante)

    // Leer los números
    for (i = 0; i < n; i++) {
        printf("Número %d: ", i + 1);
        scanf("%d", &numeros[i]);
        suma += numeros[i]; // acumulamos la suma al mismo tiempo
    }

    // Mostrar la suma total
    printf("La suma de los números es: %d\n", suma);

    return 0;
}
```
#### En Java
```java
import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in); // 2. Crear un objeto Scanner
		int suma =0;

        System.out.print("Por favor, ingresa un número entero: "); // 3. Solicitar al usuario
        int numeroEntero = scanner.nextInt();
        
        
        int[] arreglo = new int[numeroEntero];
        
        for(int i=0;i < numeroEntero; i++){
            System.out.print("Número " + (i + 1) + ": "); 
            arreglo[i] = scanner.nextInt();
            suma += arreglo[i];
        }
        
         System.out.print("La suma total es: " + suma);
        
        scanner.close();
	}
}
```
#### En Python

```python
n = int(input("¿Cuántos números querés ingresar?: "))

numeros = []
suma = 0

# Leer los números
for i in range(n):
    num = int(input(f"Número {i+1}: "))
    numeros.append(num)
    suma += num

# Mostrar el resultado
print("La suma de los números es:", suma)
```

---

### 📌 Ejercicio 3: Máximo y Mínimo en un arreglo/lista

Escribí un programa que:

1. Pida al usuario cuántos números quiere ingresar.
2. Lea esos números y los guarde en un arreglo/lista.
3. Determine el **número mayor** y el **número menor**.
4. Muestre ambos resultados por pantalla.

---

#### En C

```c
#include <stdio.h>

int main()
{
    int miNumero,i;
    int min, max;
    printf("Ingrese el tamanio del array: ");
    scanf("%d", &miNumero);
    
    if (miNumero >1){
        
        int arreglo[miNumero];
    
        for(i=0; i < miNumero; i++){
            printf("Ingrese el numero %d: ",i+1);
            scanf("%d", &arreglo[i]);
        }
        
        max = arreglo[0];
        min = arreglo[0];
        
        for(i=0; i < miNumero; i++){
            if(arreglo[i] > max){
                max = arreglo[i];
            }
            else if(arreglo[i]<min){
                min = arreglo[i];
            }
        }
        
        printf("El numero mas grande es: %d\n",max);
        printf("El numero mas chico es: %d\n",min);
        
    }
    else{
        printf("El numero para el arreglo tiene que ser mayor a  1");
    }
    
    return 0;
}
```
#### En Python
```python
n = int(input("¿Cuántos números querés ingresar?: "))

if n >1:
    numeros = []

    # Leer los números
    for i in range(n):
        num = int(input(f"Número {i+1}: "))
        numeros.append(num)
        
    mayor = numeros[0]
    menor = numeros[0]
    
    for n in numeros:
        if n > mayor:
            mayor = n
        elif n < menor:
            menor = n
    

    # Mostrar el resultado
    print("El numero mas grande es: ", mayor)
    print("El numero mas chico es: ", menor)

else:
    print("El numero para el arreglo tiene que ser mayor a 1")
```

#### En Java
```java
import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in); // 2. Crear un objeto Scanner
		int suma =0;

        System.out.print("Por favor, ingresa un número entero: "); // 3. Solicitar al usuario
        int numeroEntero = scanner.nextInt();
        
        if (numeroEntero > 1){
            int[] arreglo = new int[numeroEntero];
            for(int i=0;i < numeroEntero; i++){
            System.out.print("Número " + (i + 1) + ": "); 
            arreglo[i] = scanner.nextInt();
            }
            int max = arreglo[0];
            int min = arreglo[0];
            
            for (int n : arreglo){
                if (n > max){
                    max = n;
                }
                else if( n < min){
                    min = n;
                }
            }
            
            System.out.print("El numero mas grande es: "+ max);
            System.out.print("El numero mas chico es: "+ min);
        
            
        }
        else{
            System.out.print("El numero para el arreglo tiene que ser mayor a  1");
        }

        scanner.close();
	}
}
```

## 🌐 Ejercicio IoT 9 (en **C**)

**Empaquetado de datos de sensores en un frame binario** 📦

En muchos sistemas IoT (con LoRa, ESP-NOW, Zigbee, etc.) los datos de sensores se mandan en un **frame compacto** para ahorrar ancho de banda. Queremos armar un frame simple.

👉 Requisitos:

1. Suponé que tenemos 3 sensores:

   * Temperatura (entero, °C).
   * Humedad (entero, %).
   * Luminosidad (entero, 0-1023).
2. Pedir al usuario ingresar un valor para cada sensor.
3. Armar un **frame de 5 bytes** con el siguiente formato:

   ```
   Byte 0 → Temperatura (0-255)
   Byte 1 → Humedad (0-100)
   Byte 2 → Luminosidad parte alta (bits 8-9)
   Byte 3 → Luminosidad parte baja (bits 0-7)
   Byte 4 → Checksum (suma de bytes 0-3 módulo 256)
   ```
4. Mostrar el frame en **hexadecimal**.

---

📌 Ejemplo esperado:

```
Entrada: Temp=25, Hum=60, Lum=800
Frame (hex): [19, 3C, 03, 20, 78]
```

* `25 decimal = 0x19`
* `60 decimal = 0x3C`
* `800 decimal = 0x0320` → parte alta = `0x03`, parte baja = `0x20`
* Checksum = (0x19+0x3C+0x03+0x20) mod 256 = `0x78`

---

👉 Con este ejercicio vas a practicar:

* Manejo de enteros y arrays en C.
* Operaciones de bits (shift, máscara).
* Cálculo de checksum.
* Un caso real de **formato de comunicación IoT**.

---
```c
#include <stdio.h>
#include <stdint.h>

int main()
{
    int temp;
    int hum;
    int lum;
    uint8_t frame[5];

    printf("Ingrese la temperatura (°C, 0–255): ");
    scanf("%d", &temp);
    printf("Ingrese la humedad (0–100): ");
    scanf("%d", &hum);
    printf("Ingrese la luminosidad (0–1023): ");
    scanf("%d", &lum);

    // Empaquetado
    frame[0] = (uint8_t) temp;
    frame[1] = (uint8_t) hum;
    frame[2] = (lum >> 8) & 0xFF;   // parte alta
    frame[3] = lum & 0xFF;          // parte baja
    frame[4] = (frame[0] + frame[1] + frame[2] + frame[3]) % 256; // checksum

    // Mostrar frame
    printf("Frame generado (hex): [");
    for (int i = 0; i < 5; i++) {
        printf("%02X", frame[i]);
        if (i < 4) {
            printf(", ");
        }
    }
    printf("]\n");

    return 0;
}
```

----
## 🌐 Ejercicio IoT 10 (en **C**, usando `struct`)

**Frame de estado de dispositivo** 📡

Queremos representar el estado de un **nodo IoT** en un frame binario de **4 bytes**.

👉 Formato del frame:

* **Byte 0** → `device_id` (0–255).
* **Byte 1** → `flags` (cada bit representa un estado):

  * Bit 0 → Sensor activo (1=activo, 0=inactivo).
  * Bit 1 → Batería baja.
  * Bit 2 → Error de comunicación.
  * Bit 3–7 → Reservado.
* **Byte 2** → Nivel de batería (0–100%).
* **Byte 3** → Checksum (suma de los primeros 3 bytes mod 256).

---

### Requisitos

1. Usar un `struct` para representar el frame:

   ```c
   typedef struct {
       uint8_t device_id;
       uint8_t flags;
       uint8_t battery;
       uint8_t checksum;
   } Frame;
   ```
2. Pedir al usuario:

   * `device_id` (0–255).
   * Si el sensor está activo o no.
   * Si hay batería baja.
   * Si hay error de comunicación.
   * Nivel de batería.
3. Armar el `flags` combinando bits con operaciones de **bitwise OR (`|`)** y **shift (`<<`)**.
4. Calcular el checksum.
5. Mostrar el frame en **hexadecimal**.
6. (Opcional) Decodificar de vuelta: imprimir el estado de cada flag a partir del byte `flags`.

---

### 📌 Ejemplo esperado

Entrada:

```
Device ID: 42
Sensor activo? (1/0): 1
Batería baja? (1/0): 0
Error de comunicación? (1/0): 1
Nivel de batería (0–100): 85
```

Salida:

```
Frame (hex): [2A, 05, 55, 84]
Decodificación:
 - Sensor activo = ON
 - Batería baja = NO
 - Error de comunicación = SÍ
 - Nivel batería = 85 %
```

---

👉 Con este problema vas a practicar:

* Uso de `struct` en C.
* Manejo de bits (`|`, `<<`, `&`, `>>`).
* Checksum simple.
* Serialización y deserialización, muy típico en protocolos IoT (LoRa, Zigbee, ESP-NOW).

---



