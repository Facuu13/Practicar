#include <iostream>
#include <vector>

struct Empleado{
    std::string nombre;
    int edad;
    double salario;
};

int main()
{   
    std::vector<Empleado> empleados;
    Empleado e1;
    int cantidad = 3;
    double valor;
    
    std::cout << "Ingrese los datos de los empleados. " << std::endl;
    
    for (int i = 0; i < cantidad; i++) {
        
        std::cout << "Empleado " << i + 1 << ". " << std::endl;
        std::cout << "Nombre: ";
        std::cin >> e1.nombre;
        std::cout << "Edad: ";
        std::cin >> e1.edad;
        std::cout << "Salario: ";
        std::cin >> e1.salario;
        
        empleados.push_back(e1);
    }
    
    //El empleado con el mayor salario.
    double maximo = 0;
    int empleado;
    for (int i = 1; i <= cantidad; i++){
        if (empleados[i].salario > maximo){
            maximo = empleados[i].salario;
            empleado=i;
        }
    }
    
    std::cout << "El empleado con mayor salario es el: " << empleado+1 << ", de nombre: "  << empleados[empleado].nombre <<std::endl;

    double suma = 0;
    for (Empleado x : empleados) {
        suma += x.edad;
    }

    double promedio = suma / empleados.size();

    std::cout << "Promedio de edad: " << promedio << std::endl;

    return 0;
}