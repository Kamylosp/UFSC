#include <iostream>
#include <vector>

using namespace std;

class Animal {
public:
    virtual void move (){
        cout<<"Animal se movendo"<<endl;
    }
};

class Fish : public Animal {
    public:
        void move (){
            cout<<"Peixes se movem nadando"<<endl;
        }
};

class Frog : public Animal {
    public:
        void move (){
            cout<<"Sapos se movem pulando"<<endl;
        }
};

class Bird : public Animal {
    public:
        void move (){
            cout<<"Passaros se movem voando"<<endl;
        }
};

int main () {
    Fish nemo;
    Frog kermit;
    Bird blu;

    vector<Animal *> animals;

    animals.push_back(&nemo);
    animals.push_back(&kermit);
    animals.push_back(&blu);

    for (Animal * a_list:animals)
        a_list->move();

    return 0;
}