#include <iostream>

using std::cout;
using std::cin;
using std::endl;

//using namespace std;

int add (int n1, int n2){
    return n1+n2;
}





int main()
{
    int n1, n2;

    cout << "Enter two integers: ";
    cin >> n1 >> n2;

    cout << n1 << " + " << n2 << " = " << add(n1, n2) << endl;

    return 0;
}
