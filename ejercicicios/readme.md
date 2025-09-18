
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