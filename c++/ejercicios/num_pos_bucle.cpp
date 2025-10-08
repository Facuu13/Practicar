#include <iostream>

int main() {
    int numero;
    do{
        std::cout << "Ingresa un número: ";
        std::cin >> numero;
    }while(numero<0);
    
    for (int i=1;i<11;i++){
        std::cout << numero << " x " << i << " = " << numero*i << std::endl;
    }

    return 0;
}