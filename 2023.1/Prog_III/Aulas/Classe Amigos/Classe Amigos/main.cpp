#include <iostream>

using namespace std;

class Pessoa {
    private:
        string nome, telefone, identificador;
    public:
        void setName (string n){
            nome = n;
        }

        void setTelefone (string tel){
            telefone = tel;
        }

        void setIdentificador (string id){
            identificador = id;
        }

        string getName (){
            return nome;
        }

        string getTelefone(){
            return telefone;
        }

        string getIdentificador (){
            return identificador;
        }



};

int main() {
    Pessoa amigo1, amigo2, amigo3, amigo4;

    amigo1.setName("Lucas Barcaro");
    amigo1.setTelefone("985123");
    amigo1.setIdentificador("5");

    amigo2.setName("Pedro Dantas");
    amigo2.setTelefone("971634");
    amigo2.setIdentificador("27");

    amigo3.setName("Italo");
    amigo3.setTelefone("936521");
    amigo3.setIdentificador("12");

    amigo4.setName("Lucas Bernardino");
    amigo4.setTelefone("976214");
    amigo4.setIdentificador("19");

    cout << "Amigo 1: " << amigo1.getName() << endl;
    cout << "ID: " << amigo1.getIdentificador() << endl;
    cout << "Telefone: " << amigo1.getTelefone() << endl;

    cout << "\nAmigo 2: " << amigo2.getName() << endl;
    cout << "ID: " << amigo2.getIdentificador() << endl;
    cout << "Telefone: " << amigo2.getTelefone() << endl;

    cout << "\nAmigo 3: " << amigo3.getName() << endl;
    cout << "ID: " << amigo3.getIdentificador() << endl;
    cout << "Telefone: " << amigo3.getTelefone() << endl;

    cout << "\nAmigo 4: " << amigo4.getName() << endl;
    cout << "ID: " << amigo4.getIdentificador() << endl;
    cout << "Telefone: " << amigo4.getTelefone() << endl;
    return 0;
}
