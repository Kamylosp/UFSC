#pragma once

class Car {
    private:
        double power;
        double price;

    public:

        Car();
        Car(double _power, double _price);
        
        double getPower ();
        double getPrice ();
        void setPower (double pot);
        void setPrice (double preco);

};
