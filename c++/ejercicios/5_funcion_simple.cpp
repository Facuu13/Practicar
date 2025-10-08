#include <iostream>

void es_par(int num);

int main() {
    int numero;
    
    std::cout << "Ingresa un número: ";
    std::cin >> numero;
    
    es_par(numero);

    return 0;
}

void es_par(int num){
    if(num%2==0){
        std::cout << "El número " << num << " es par."<< std::endl ;
    }
    else{
        std::cout << "El número " << num << " es impar."<< std::endl ;
    }
}