#include "car.h"

Car::Car(){
    power = 1000;
    price = 500;
}

Car::Car(double _power, double _price){
    power = _power;
    price = _price;
}

double Car::getPower(){
    return power;
}
double Car::getPrice (){
    return price;
}
void Car::setPower (double pot){
    power = pot;
}
void Car::setPrice (double preco){
    price = preco;
}
