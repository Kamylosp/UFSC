#include "car.h"
#include <iostream>
#include <string>
#include <type_traits>

using namespace std;

// Especialização do template para o tipo double
template class Car<double>;

template <typename T>
Car<T>::Car() {
    power = 1000;
    price = 500;
}

template <typename T>
Car<T>::Car(T _power, T _price) {
    power = _power;
    price = _price;
    
}

template <typename T>
Car<T>& Car<T>::operator=(const Car& obj) {
    power = obj.power + 1;
    price = obj.price + 1;
    cout << "assignment operator" << endl;
    return *this;
}

template <typename T>
Car<T>::~Car() {
    cout << "custom destructor" << endl;
    cout << "Power: " << getPower() << endl;
    cout << "Price: " << getPrice() << endl;
        
}

template <class T>
T Car<T>::getPower() {
    return power;
}

template <class T>
T Car<T>::getPrice() {
    return price;
}

template <class T>
Car<T>& Car<T>::setPower(T pot) {
    power = pot;
    return *this;
        
}

template <class T>
Car<T>& Car<T>::setPrice(T preco) {
    price = preco;
    return *this;
}

template <class T>
void Car<T>::printAdress() {
    cout << "Class address: " << this << endl;
}

template <class T>
void Car<T>::showInfo() const {
    cout << "Power: " << power << endl;
    cout << "Price: " << this->price << endl;
}

template <class T>
T Car<T>::getSpeed() {
    return speed;
}

template <class T>
void Car<T>::setSpeed(T spd) {
    speed = spd;
}

template <class T>
void Car<T>::acelerate(T newSpeed) {
    setSpeed(newSpeed);
}

template <class T>
void Car<T>::acelerate(int newSpeed) {
    setSpeed(newSpeed);
}

template <class T>
void Car<T>::acelerate(string maxmin) {
    if (maxmin == "max")
        setSpeed(120);
    else if (maxmin == "min")
        setSpeed(60);
}

template <class T>
void Car<T>::acelerate(T timeAcell, T acellerate) {
    setSpeed(getSpeed() + timeAcell * acellerate * 3.6);
}

template <class T>
void Car<T>::acelerate(char* newSpeed) {
    setSpeed(atof(newSpeed));
}