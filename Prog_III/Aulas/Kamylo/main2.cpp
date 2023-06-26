#include <iostream>
#include <string>
#include<iomanip>


using namespace std;

class PhoneNumber {
    friend ostream &operator<<(ostream &, const PhoneNumber &);
    friend istream &operator>>(istream &, PhoneNumber &);

    private:
        string areaCode;
        string exchange;
        string line;
};

ostream &operator<<(ostream &output, const PhoneNumber &number){
    output << "(" << number.areaCode << ") "
            << number.exchange << "-"<<number.line;
        
    return output;
}

istream &operator>> (istream &input, PhoneNumber &number){
    input.ignore();
    input >> setw(3) >> number.areaCode;
    input.ignore(2);
    input >> setw(3) >> number.exchange;
    input.ignore();
    input >> setw(4) >> number.line;

    return input;

}


int main (){
    PhoneNumber numero;

    cin >> numero;

    cout<< "Meu numero e: "<< numero << endl;


    return 0;
}