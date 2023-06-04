/*
Aluno: Kamylo Serafim Porto
Turma: Sexta Feira
*/

#include <iostream>
#include <type_traits>
#include <string>

using namespace std;

template <class T>
class Car {
    private:
        T power;   
        T price;
        T speed = 0;

    public:
        Car();
        Car(T _power, T _price);
        Car(const Car & obj); 

        Car & operator=(const Car & obj);
        ~Car();
        
        T getPower ();
        T getPrice ();

        Car &setPower (T pot);
        Car &setPrice (T preco);
        
        void printAdress();
        void showInfo () const;

        T getSpeed();
        void setSpeed(T spd);

        void acelerate(T newSpeed);
        void acelerate(std::string maxmin);
        void acelerate(T timeAcell, T acellerate);
        void acelerate(char *newSpeed);
};

// Função main
int main(){
    Car<float> Ferrari(596, 760000);
    cout << endl <<"\n<float> Ferrari:" << endl;
    Ferrari.showInfo();

    Car<double> Audi(260, 230000);
    cout << endl <<"\n<double> Audi:" << endl;
    Audi.showInfo();

    Car<char> Mercedes(242,349999);
    cout <<endl<< "\n<char> Mercedes:" << endl;
    Mercedes.showInfo();

    cout << "\n\n----------------\n\n"<<endl;
    
    return 0;
}


template <typename T>
Car<T>::Car() {
    power = 150;
    price = 100000;
}

template <typename T>
Car<T>::Car(T _power, T _price) {
    if (is_floating_point<T>::value) {
        power = _power;
        price = _price;
    }
}

template<typename T>
Car<T> :: Car(const Car & obj){
    power = obj.Power;
    price = obj.Price;
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
    if (is_floating_point<T>::value){
        cout << "Power: " << getPower() << endl;
        cout << "Price: " << getPrice() << endl;
    }
        
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
    if (is_floating_point<T>::value){
        cout << "Power: " << power << endl;
        cout << "Price: " << this->price << endl;
    } else
        cout << "Variavel do tipo invalido!"<<endl;
}

template <class T>
T Car<T>::getSpeed() {
    return speed;
}

template <class T>
void Car<T>::setSpeed(T spd) {
    speed = (T) spd;
}

template <class T>
void Car<T>::acelerate(T newSpeed) {
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

