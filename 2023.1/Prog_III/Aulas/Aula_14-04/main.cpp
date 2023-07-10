#include <iostream>

using namespace std;

int main (){
    int num = 3;

    cout << "Numero: " << num << endl;
    cout << "End de num: " << &num << endl;

    int *p_num = &num;
    cout << "Numero: " << *p_num << endl;
    cout << "End de num: " << p_num << endl;
    cout << "End de p_num: " << &p_num << endl;




}