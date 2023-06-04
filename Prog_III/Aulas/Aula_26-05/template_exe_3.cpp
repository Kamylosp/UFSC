#include <iostream>
#include <vector>
#include <cstdlib>
#include <string>
#include <stdexcept>
#include "car.h"

using namespace std;

template <class T>
    class Stack {
        private:
            vector<T> elems;
        
        public:
            void push(T const&);
            void pop();
            T top () const;

            bool empty() const {
                return elems.empty();
            }

            void returncontent();
    };

template <>
    class Stack <Car> {
        private:
            vector<Car> elems;
        
        public:
            void push(double, double);

            void returncontent();
    };

    
int main (){

    Stack <int> intStack;
    Stack <string> stringStack;
    Stack <Car> carStack;

    intStack.push(1);
    intStack.push(8);
    intStack.push(4);
    intStack.push(0);
    intStack.push(5);
    //intStack.push(0);
    intStack.returncontent();

    stringStack.push("A");
    stringStack.push("B");
    stringStack.push("C");
    stringStack.push("D");
    stringStack.push("E");
    stringStack.push("");
    stringStack.returncontent();


    carStack.push(450, 66000);
    carStack.push(375, 134000);
    carStack.push(320, 108000);
    carStack.push(350, 83000);
    carStack.push(345, 42000);
    carStack.returncontent();

    return 0;
}

template <class T>
void Stack<T>::push (T const& elem){
    elems.push_back(elem);
}

template <class T>
void Stack<T>::pop (){
    if (elems.empty()){
        throw out_of_range("Stack<>::pop: empty stack");
    }

    elems.pop_back();
}

template <class T>
T Stack<T>::top () const {
    if (elems.empty()){
        throw out_of_range("Stack<>::top: empty stack");
    }

    elems.back();
}

template <class T>
void Stack<T>::returncontent (){
    for (unsigned int i=0; i<elems.size(); i++)
        cout << elems[i]<<endl;
}

void Stack<Car>::push (double pwr, double prc){
    Car carro(pwr, prc);

    elems.push_back(carro);
}

void Stack<Car>::returncontent (){
    for (unsigned int i=0; i<elems.size(); i++){
        cout << "Price: " << elems[i].getPrice();
        cout << "      Power: "<<elems[i].getPower()<<endl;
    }
}