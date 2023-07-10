#include <iostream>
using namespace std;

template <typename T>
    T square(T y ) {
        cout << "Square of " << y << " is ";
        return y * y;
    }

int main (){
    cout << square(7) << endl;
    cout << square(7.5) << endl;

    cout << square<int>(7) << endl;
    cout << square<int>(7.5) << endl;

}