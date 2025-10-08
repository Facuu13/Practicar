#include <iostream>
#include <string>

int main() {
    int edad;
    std::string nombre;
    double altura;

    std::cout << "Ingresa tu nombre: ";
    //std::cin >> nombre;   // lee una palabra (sin espacios)
    std::getline(std::cin, nombre); // lee una linea completa (con espacios)
    
    std::cout << "Ingresa tu edad: ";
    std::cin >> edad;
    
    std::cout << "Ingresa tu altura (en metros): ";
    std::cin >> altura;

    std::cout << "\nHola " << nombre << ", tienes " << edad
              << " anios, mides " << altura << " metros y naciste en el anio " << 2025-edad << std::endl;

    return 0;
}
