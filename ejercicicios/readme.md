
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