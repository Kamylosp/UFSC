#include <iostream>

using namespace std;

class GradeBook {
public:
    void setCourseName (string n);
    string getCourseName ();
    void displayMessage (string texto);

private:
    string name;
};


int main()
{
    GradeBook objeto;
    string txt, output;
    txt = "Kamylo";

    objeto.setCourseName(txt);
    output = objeto.getCourseName();

    objeto.displayMessage(output);
    return 0;
}

void GradeBook::setCourseName (string n){
    name = n;
}
string GradeBook::getCourseName (){
    return name;
}

void GradeBook::displayMessage (string texto){
    cout << "O texto e: " << texto << endl;
}
