/*
Aluno: Kamylo Serafim Porto
Turma: Sexta-Feira

O código foi implementado de modo que quando o usuário tenta 
utilizar a classe como char, o programa não irá compilar e
será printado na tela um erro. Já, quando é passado um número, 
o programa funciona normalmente */


#include <iostream>
#include <string>
#include <type_traits>
#include "car.h"

using namespace std;

int main() {

    cout << is_integral<int>::value<<endl;
    cout << is_integral<char>::value<<endl;
    
    return 0;
}
