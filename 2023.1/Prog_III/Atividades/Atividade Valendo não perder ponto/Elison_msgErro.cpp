#include <iostream>
#include <string>
#include <type_traits>

using namespace std;

template<typename T>
class Car{
    static_assert(std::is_floating_point<T>::value, "Suporta apenas tipo double e float");
    public:
        Car(); // default constructor
        Car(T Power2, T Price2 ); // custom constructor
        Car(const Car & obj); 
        Car<T> & operator=(const Car & obj);
        ~Car(); // destructor

        T getPrice();
        T getPower();
        static unsigned int getNumCars();
        
        void showinfo() const;
        
        Car<T> &setPower(T Power2);
        Car<T> &setPrice(T Price2);
        
    private:
        T Power;
        T Price;
        static unsigned int number_of_cars;
};

int main(){

    Car<double> BMW(300,4000);
    cout << "<double> BMW:" << endl;
    BMW.showinfo();
    Car<float> Dodge(700, 7000);
    cout << endl <<"<float> Dodge:" << endl;
    Dodge.showinfo();
    
    Car<char> Skyline(127,475);
    cout <<endl<< "<char> Skyline:" << endl;
    Skyline.showinfo();
    
    cout<< endl << "---End---"<<endl;
    
    return 0;
}


//====================Construtores =====================
template<typename T>
Car<T> :: Car(){
    Power = 1000;
    Price = 500;
    cout << "\nDEFAULT CONSTRUCTOR" << endl;
    number_of_cars++;
}

template<typename T>
Car<T> :: Car(const Car & obj){
    Power = obj.Power;
    Price = obj.Price;
    number_of_cars++;
    cout << "\nCOPY CONSTRUCTOR" << endl;
}

template<typename T>
Car<T>::Car(T Power2, T Price2) {
    if (is_floating_point<T>::value) {
        Power = Power2;
        Price = Price2;
        number_of_cars++;
    }
}

template<typename T>
Car<T> & Car<T>::operator =(const Car & obj){
    Power = obj.Power + 1;
    Price = obj.Price + 1;
    number_of_cars++;
    cout << "\nCOPY CONSTRUCTOR" << endl;
    return *this;
}
//===============Destrutor ===================
template <class T>
Car<T>::~Car() {
    cout<<"Default Destructor"<<endl;
}
//=================Funções extras=================
template <class T>
void Car<T>::showinfo() const{
    if (is_floating_point<T>::value) {
    cout << "Power:" << Power << endl;
    cout << "Price:" << Price << endl;
        number_of_cars++;
    }else {
        cout << "INVALIDE TYPE - NOT SUPPORTED" << endl;
    }
}
template <class T>
unsigned int Car<T>::number_of_cars = 0;
//==============Funções get ==================
template<typename T>
T Car<T>::getPower(){
    return Power;
}
template<typename T>
T Car<T>::getPrice(){
    return Price;
}

template <class T>
unsigned int Car<T>::getNumCars(){
    return number_of_cars;
}

//=============Funções Set =================
template <class T>
Car<T>& Car<T>::setPower (T Power2){
    this-> Power = Power2;
}
template <class T>
Car<T>& Car<T>::setPrice (T Price2){
    this-> Price = Price2;
}









