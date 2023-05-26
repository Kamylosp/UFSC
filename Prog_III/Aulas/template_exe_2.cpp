#include <iostream>
using namespace std;

template <typename T>
    T Min(T a, T b, T c) {
        if (a < b){
            if (a < c)
                return a;
            else
                return c;
        } else{
            if (b < c)
                return b;
            else
                return c;
        }
    }

int main (){
    int i1, i2, i3;
    float f1, f2, f3;
    char s1, s2, s3;

    cout<<"insert three integers: "<<endl;
    cout<<"1: ";
    cin>>i1;
    cout<<"2: ";
    cin>>i2;
    cout<<"3: ";
    cin>>i3;

    cout<<"insert three float numbers: "<<endl;
    cout<<"1: ";
    cin>>f1;
    cout<<"2: ";
    cin>>f2;
    cout<<"3: ";
    cin>>f3;

    cout<<"insert three letters: "<<endl;
    cout<<"1: ";
    cin>>s1;
    cout<<"2: ";
    cin>>s2;
    cout<<"3: ";
    cin>>s3;

    cout<< "The minimum integer is: "<< Min(i1, i2, i3)<<endl;
    cout<< "The minimum float is: "<< Min(f1, f2, f3)<<endl;
    cout<< "The minimum string is: "<< Min(s1, s2, s3)<<endl;
}