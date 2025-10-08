#include <iostream>
#include <vector>

int main()
{   
    std::vector<double> temperaturas;
    int cantidad = 5;
    double valor;
    
    std::cout << "Ingrese 5 temperaturas." << std::endl;
    
    for (int i = 0; i < cantidad; i++) {
        std::cout << "temperatura " << i + 1 << ": ";
        std::cin >> valor;
        temperaturas.push_back(valor);
    }
    double maximo =temperaturas[0];
    double minimo = temperaturas[0];
    double suma = 0;
    for (double x : temperaturas) {
        suma += x;
        if (x>maximo){
            maximo = x;
        }
        else if (x< minimo){
            minimo = x;
        }
    }

    double promedio = suma / temperaturas.size();

    std::cout << "Promedio de temperatura: " << promedio << std::endl;
    
    std::cout << "La mayor temperatura es: " << maximo << std::endl;
    
    std::cout << "La menor temperatura: " << minimo << std::endl;

    return 0;
}