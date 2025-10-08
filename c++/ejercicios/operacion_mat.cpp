#include <iostream>

int main()
{
    int numero1;
    int numero2;
    char operacion;
    
    std::cout<<"Ingresa primer número: ";
    std::cin>>numero1;
    std::cout<<"Ingresa segundo número: ";
    std::cin>>numero2;
    
    std::cout<<"Ingresa primer número: ";
    std::cin>>operacion;
    
    switch(operacion){
        case '+':
            std::cout << "El resultado de la suma es: " << numero1 + numero2 << std::endl;
            break;
        case '-':
            std::cout << "El resultado de la resta es: " << numero1 - numero2 << std::endl;
            break;
        case '*':
            std::cout << "El resultado de la multiplacacion es: " << numero1 * numero2 << std::endl;
            break;
        case '/':
            if (numero2 != 0){
                std::cout << "El resultado de la division es: " << numero1 / numero2 << std::endl;
                break;
            }
            else{
                std::cout << "No se puede dividir por cero." << std::endl;
                break;
            }
            
        default:
           std::cout << "Operación no válida. Use +, -, *, /" << std::endl;
    }
    return 0;
}