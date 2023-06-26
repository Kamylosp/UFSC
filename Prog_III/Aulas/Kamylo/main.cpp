#include <iostream>
#include "car.h"

using namespace std;

int main (){
    Car audi(120, 100000);
    Car ferrari(510, 500000);
    Car newcar;

    //newcar = audi.operator+(ferrsari);
    newcar = audi + ferrari;
    newcar = audi.operator+(ferrari);
    cout<<"show info"<<endl;
    newcar.showInfo();

    cout<<"Qual e maior: " << ((audi>ferrari) ? "audi" : "ferrari") <<endl;

}