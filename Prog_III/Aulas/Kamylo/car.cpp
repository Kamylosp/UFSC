#include "car.h"
#include <iostream>
#include <string>

Car::Car(){
    power = 1000;
    price = 500;
}

Car::Car(double _power, double _price){
    power = _power;
    price = _price;
}

Car & Car::operator=(const Car & obj){
    power = obj.power;
    price = obj.price;
    //std::cout << "assignment operator" << std::endl;
    return *this;
}

Car::~Car (){
    //std::cout << "custom destructor" << std::endl;
    //std::cout << "Price: " << getPrice() << std::endl;
    //std::cout << "Power: " << getPower() << std::endl;
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

Car Car::operator+ (const Car &obj){
    Car temp;
    temp.power = power + obj.power;
    temp.price = price + obj.price;
    return temp;
}

bool Car::operator> (const Car &obj){
    double FoM1 = power/price;
    double FoM2 = obj.power/obj.price;

    if (FoM1 > FoM2) return true;
    else return false;
}
bool Car::operator< (const Car &obj){
    double FoM1 = power/price;
    double FoM2 = obj.power/obj.price;

    //return 
    if (FoM1 < FoM2) return true;
    else return false;
}


void Car::printAdress (){
    std::cout << "Class adress: " << this << std::endl;
}

void Car::showInfo () const {
    std::cout << "Power: " << power << std::endl;
    std::cout << "Price: " << this->price << std::endl;
}


double Car::getSpeed(){
    return speed;
}

void Car::setSpeed(double spd){
    speed = spd;
}

void Car::acelerate(int newSpeed){
    setSpeed(newSpeed);
}

void Car::acelerate(double newSpeed){
    setSpeed(newSpeed);
}

void Car::acelerate(std::string maxmin){
    if (maxmin == "max")
        setSpeed(120);
    else if (maxmin == "min")
        setSpeed(60);
}

void Car::acelerate(double timeAcell, double acellerate){
    setSpeed(getSpeed() + timeAcell * acellerate * 3.6);
}

void Car::acelerate(char *newSpeed){
    setSpeed(atof(newSpeed));
}