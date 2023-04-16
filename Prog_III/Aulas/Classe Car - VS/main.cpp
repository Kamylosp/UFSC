#include <iostream>
#include "car.h"
using namespace std;

/*Car *CreateCarStandard (){
    Car *car = new Car;
    cout << "adress car: " << car << endl;
    cout << "pricec car: " << car->getPrice() << endl;

    return car;
}*/

int main()
{
    Car BMW(1200, 100);

    cout << BMW.getPower() << endl;
    cout << BMW.getPrice() << endl;


    /*   
    Car*c = CreateCarStandard();

    cout << "value c: " << c << endl;
    cout << "adress c: " << &c << endl;

    double price = c->getPrice();
    cout << "Price: " << price << endl;
    return 0;*/
}
