/******************************************************************************

Gestión de ventas diarias”
Una tienda registra las ventas del día.
Cada venta tiene:
un ID de producto
una cantidad vendida
un precio unitario

Se pide un programa que:
Permita ingresar los datos de 4 ventas.
Calcule para cada una el importe total (cantidad * precio).

Muestre todas las ventas con formato:
ID - cantidad - precio - total
Calcule y muestre el total general del día (la suma de todos los importes).
Muestre el producto con mayor importe de venta individual.

Ingrese ID del producto 1: 1001
Cantidad vendida: 3
Precio unitario: 250.50

Ingrese ID del producto 2: 1002
Cantidad vendida: 1
Precio unitario: 520.00
...

Ventas del día:
ID     Cantidad    Precio     Total
1001      3        250.50     751.50
1002      1        520.00     520.00
1003      5        100.00     500.00
1004      2        300.00     600.00

Total general del día: $2371.50
Venta individual más alta: producto 1001 ($751.50)


*******************************************************************************/
#include <iostream>
#include <vector>

struct Producto{
    int id;
    int cantidad;
    double precio;
};

int main()
{
    std::vector<Producto> productos;
    Producto p1;
    
    for (int i = 0; i < 4; i++){
        std::cout << "Ingrese ID del producto " << i + 1 << ": ";
        std::cin >> p1.id;
        std::cout << "Cantidad vendida: ";
        std::cin >> p1.cantidad;
        std::cout << "Precio unitario: ";
        std::cin >> p1.precio;
        productos.push_back(p1);
    }
    
    std::cout << "Ventas del día: " << std::endl;
    std::cout << "ID     Cantidad    Precio     Total " << std::endl;
    double total_general=0;
    int producto_id = 0;
    double precio_producto=0;
    for (Producto p : productos){
        double precio_total = p.precio * p.cantidad;
        total_general = total_general + precio_total;
        if(precio_total > precio_producto){
            precio_producto = precio_total;
            producto_id = p.id;
        }
        std::cout << p.id  << "     " << p.cantidad << "     " << p.precio << "     " << precio_total << std::endl;
    }
    std::cout << "Total general del día: " << total_general << std::endl;
    std::cout << "Venta individual más alta: producto " << producto_id << "($" << precio_producto << ")" << std::endl;

    return 0;
}