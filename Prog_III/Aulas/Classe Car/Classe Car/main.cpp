#include <iostream>

using namespace std;

class Car {
    private:
        double Power;
        double price;

    public:
        double getPower ();

};

int main() {
    Car BMW;
    double Power_BMW = BMW.getPower();

    cout << "Potencia: " << Power_BMW << endl;
}


double Car::getPower(){
    Power = 1000;
    return Power;
}
