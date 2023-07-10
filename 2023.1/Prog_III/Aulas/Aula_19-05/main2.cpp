#include <iostream>
using namespace std;

template <typename T>
    T add(T x, T y, T z=0) {
        return x + y + z;
    }

int main() {
    cout << add(5, 3) << endl;

    return 0;
}