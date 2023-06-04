#include <iostream>
#include <type_traits>
#include <string>

template <class T>
class Car {
    static_assert(std::is_floating_point<T>::value, "Apenas variaveis numericas!");
    private:
        T power;   
        T price;
        T speed = 0;

    public:
        Car();
        Car(T _power, T _price);

        Car & operator=(const Car & obj);
        ~Car();
        
        T getPower ();
        T getPrice ();
        // void setPower (T pot);
        // void setPrice (T preco);

        Car &setPower (T pot);
        Car &setPrice (T preco);
        
        void printAdress();
        void showInfo () const;

        T getSpeed();
        void setSpeed(T spd);

        void acelerate(T newSpeed);
        void acelerate(int newSpeed);
        void acelerate(std::string maxmin);
        void acelerate(T timeAcell, T acellerate);
        void acelerate(char *newSpeed);
};