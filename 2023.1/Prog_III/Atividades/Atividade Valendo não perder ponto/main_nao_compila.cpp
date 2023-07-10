/* Aluno: Kamylo Serafim Porto

    Este programa não irá compilar pois as type traits foram implementadas
    de modo que não seja possível 



*/


#include <iostream>
#include <string>
#include <type_traits>
#include "car.h"

using namespace std;

int main() {
    Car<char> Ferrari(123, 150);

    Ferrari.showInfo();
    
    return 0;
}
