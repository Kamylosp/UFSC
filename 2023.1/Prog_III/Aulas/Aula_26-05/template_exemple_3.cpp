#include <iostream>
#include <vector>
#include <cstdlib>
#include <string>
#include <stdexcept>

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

int main (){
    Stack <int> intStack;
    Stack <string> stringStack;

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