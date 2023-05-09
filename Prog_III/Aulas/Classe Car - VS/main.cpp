#include <iostream>
#include "car.h"
using namespace std;

// g++ main.cpp car.cpp -o main.exe

void test (Car object){
    cout << "Price of BMW in the test function is: " << object.getPrice() << endl;
}

int main()
{
    Car BMW(328, 41245);

    cout << "Power of BMW is: " << BMW.getPower() << endl;
    cout << "Price of BMW is: " << BMW.getPrice() << endl;
    cout << "------" << endl;
/*
    Car BMW2;
    cout << "Power of BMW2 is: " << BMW2.getPower() << endl;
    cout << "Price of BMW2 is: " << BMW2.getPrice() << endl;
    cout << "------" << endl;

    BMW2 = BMW;
    cout << "Power of BMW2 is: " << BMW2.getPower() << endl;
    cout << "Price of BMW2 is: " << BMW2.getPrice() << endl;
    cout << "------" << endl;
    BMW2.printAdress();
*/
/*
    Car *Ferrari = new Car(1234, 123456);
    delete Ferrari;
*/
    BMW.setPower(1000).setPrice(150000);
    BMW.showInfo();

}