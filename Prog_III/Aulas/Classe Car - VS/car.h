#pragma once

class Car {
    private:
        double power;
        double price;

    public:

        Car();
        Car(double _power, double _price);

        Car & operator=(const Car & obj);
        ~Car();
        
        double getPower ();
        double getPrice ();
        // void setPower (double pot);
        // void setPrice (double preco);

        Car &setPower (double pot);
        Car &setPrice (double preco);
        
        void printAdress();
        void showInfo () const;

};
