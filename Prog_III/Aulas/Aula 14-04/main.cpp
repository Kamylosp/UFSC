#include <iostream>
#include "car.h"
using namespace std;

int main()
{
    Car BMW, ferrari, audi, mercedes;
    BMW.setPower(382);
    BMW.setPrice(41245);
    cout << "Potencia BMW: " << BMW.getPower() << " hp" << endl;
    cout << "Preco BMW: U$ " << BMW.getPrice() << endl;

    ferrari.setPower(710);
    ferrari.setPrice(350000);
    cout << "\nPotencia Ferrari: " << ferrari.getPower() << " hp" << endl;
    cout << "Preco Ferrari: U$ " << ferrari.getPrice() << endl;

    audi.setPower(402);
    audi.setPrice(74800);
    cout << "\nPotencia Audi: " << audi.getPower() << " hp" << endl;
    cout << "Preco Audi: U$ " << audi.getPrice() << endl;

    mercedes.setPower(410);
    mercedes.setPrice(95800);
    cout << "\nPotencia Mercedes: " << mercedes.getPower() << " hp" << endl;
    cout << "Preco Mercedes: U$ " << mercedes.getPrice() << endl;
}
