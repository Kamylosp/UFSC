#include "car.h"
#include <iostream>

Car::Car(){
    power = 1000;
    price = 500;
}

Car::Car(double _power, double _price){
    power = _power;
    price = _price;
}

Car & Car::operator=(const Car & obj){
    power = obj.power + 1;
    price = obj.price + 1;
    std::cout << "assignment operator" << std::endl;
    return *this;
}

Car::~Car (){
    std::cout << "custom destructor" << std::endl;
    std::cout << "Price: " << getPrice() << std::endl;
    std::cout << "Power: " << getPower() << std::endl;
}

double Car::getPower(){
    return power;
}
double Car::getPrice (){
    return price;
}
// void Car::setPower (double pot){
//     power = pot;
// }
// void Car::setPrice (double preco){
//     price = preco;
// }

Car & Car::setPower (double pot){
    power = pot;
    return *this;
}
Car & Car::setPrice (double preco){
    price = preco;
    return *this;
}

void Car::printAdress (){
    std::cout << "Class adress: " << this << std::endl;
}

void Car::showInfo () const {
    std::cout << "Power: " << power << std::endl;
    std::cout << "Price: " << this->price << std::endl;
}
