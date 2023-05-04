#include <iostream>
#include <string>

class Calculadora
{
private:
    float num1;
    float num2;
    float memoria;
    bool memoria_limpa = true;
public:
    Calculadora(float memoria);
    float soma();
    float subtracao();
    float multiplicacao();
    float divisao();
    void limpa_memoria();
    std::string menu();
    float returnMemoria();
    void verifica_operacao(std::string escolha, char* ptr);
    bool converte(std::string* num, float* num_float);
};


int main(){
    Calculadora calc(0.0);
    char number = '1';
    while (number == '1')
    {
        std::string escolha = calc.menu();
        calc.verifica_operacao(escolha, &number);
    }
    return 0;
}

bool Calculadora::converte(std::string* num, float* num_float)
{
    try
    {
        *num_float = std::stof(*num);
        return true;
    }
    catch (std::invalid_argument)
    {
        std::cout<<"\nOperacao Invalida.\nDigite um numero.\n"<<std::endl;
        return false;
    }
}

void Calculadora::verifica_operacao(std::string escolha, char* ptr)
{
        if (escolha == "c" || escolha == "C")
        {
            this->limpa_memoria();

        }
        else if (escolha == "+")
        {
            this->soma();

        }
        else if (escolha == "-")
        {
            this->subtracao();

        }
        else if (escolha == "*")
        {
            this->multiplicacao();

        }
        else if (escolha == "/")
        {
            this->divisao();
        }
        else if (escolha == "s" || escolha == "S")
        {
            std::cout<<"===================  FIM DO PROGRAMA  ==================="<<std::endl;
            *ptr = 0;
        }
        else
        {
            std::cout<<"===================  Operacao Invalida  =================="<<std::endl;
        }
}

Calculadora::Calculadora(float memoria)
{
    this->memoria = memoria;
}

float Calculadora::soma()
{
    std::string n1;
    std::string n2;
    float num_float;
    if (this->memoria_limpa == true)
    {
        bool teste_converte = false;
        while (!teste_converte)
        {
            std::cout<<"Digite o primeiro numero: ";
            std::cin>>n1;
            teste_converte = this->converte(&n1, &num_float);
            if (teste_converte == false) continue;
            this->num1 = num_float;
            std::cout<<"Digite o segundo numero: ";
            std::cin>>n2;
            teste_converte = this->converte(&n2, &num_float);
            if (teste_converte == false) continue;
            this->num2 = num_float;
            this->memoria = this->num1 + this->num2;
            std::cout<<"\nResultado: "<<this->num1<<" + "<<this->num2<<" = "<<this->memoria<<std::endl;
        }
    }
    if (this->memoria_limpa == false)
    {
        bool teste_converte = false;
        while (!teste_converte)
        {
            std::cout<<"Digite o numero para somar com o da memoria: ";
            std::cin>>n1;
            teste_converte = this->converte(&n1, &num_float);
            if (teste_converte == false) continue;
            this->num1 = num_float;
            this->num2 = this->memoria;
            this->memoria = this->num2 + this->num1;
            std::cout<<"\nResultado: "<<this->num2<<" + "<<this->num1<<" = "<<this->memoria<<std::endl;
        }
    }
    this->memoria_limpa = false;
    return this->memoria;
}

float Calculadora::subtracao()
{
    std::string n1;
    std::string n2;
    float num_float;
    if (this->memoria_limpa == true)
    {
        bool teste_converte = false;
        while (!teste_converte)
        {
            std::cout<<"Digite o primeiro numero: ";
            std::cin>>n1;
            teste_converte = this->converte(&n1, &num_float);
            if (teste_converte == false) continue;
            this->num1 = num_float;
            std::cout<<"Digite o segundo numero: ";
            std::cin>>n2;
            teste_converte = this->converte(&n2, &num_float);
            if (teste_converte == false) continue;
            this->num2 = num_float;
            this->memoria = this->num1 - this->num2;
            std::cout<<"\nResultado: "<<this->num1<<" - "<<this->num2<<" = "<<this->memoria<<std::endl;
        }
    }
    if (this->memoria_limpa == false)
    {
        bool teste_converte = false;
        while (!teste_converte)
        {
            std::cout<<"Digite o numero para subtrair com o da memoria: ";
            std::cin>>n1;
            teste_converte = this->converte(&n1, &num_float);
            if (teste_converte == false) continue;
            this->num1 = num_float;
            this->num2 = this->memoria;
            this->memoria = this->num2 - this->num1;
            std::cout<<"\nResultado: "<<this->num2<<" - "<<this->num1<<" = "<<this->memoria<<std::endl;
        }
    }
    this->memoria_limpa = false;
    return this->memoria;
}

float Calculadora::multiplicacao()
{
    std::string n1;
    std::string n2;
    float num_float;
    if (this->memoria_limpa == true)
    {
        bool teste_converte = false;
        while (!teste_converte)
        {
            std::cout<<"Digite o primeiro numero: ";
            std::cin>>n1;
            teste_converte = this->converte(&n1, &num_float);
            if (teste_converte == false) continue;
            this->num1 = num_float;
            std::cout<<"Digite o segundo numero: ";
            std::cin>>n2;
            teste_converte = this->converte(&n2, &num_float);
            if (teste_converte == false) continue;
            this->num2 = num_float;
            this->memoria = this->num1 * this->num2;
            std::cout<<"\nResultado: "<<this->num1<<" * "<<this->num2<<" = "<<this->memoria<<std::endl;
        }
    }
    if (this->memoria_limpa == false)
    {
        bool teste_converte = false;
        while (!teste_converte)
        {
            std::cout<<"Digite o numero para multiplicar com o da memoria: ";
            std::cin>>n1;
            teste_converte = this->converte(&n1, &num_float);
            if (teste_converte == false) continue;
            this->num1 = num_float;
            this->num2 = this->memoria;
            this->memoria = this->num2 * this->num1;
            std::cout<<"\nResultado: "<<this->num2<<" * "<<this->num1<<" = "<<this->memoria<<std::endl;
        }
    }
    this->memoria_limpa = false;
    return this->memoria;
}

float Calculadora::divisao() //Não esquecer da divisão por 0.
{
    std::string n1;
    std::string n2;
    float num_float;
    if (this->memoria_limpa == true)
    {
        bool teste_converte = false;
        while (!teste_converte)
        {
            std::cout<<"Digite o primeiro numero: ";
            std::cin>>n1;
            teste_converte = this->converte(&n1, &num_float);
            if (teste_converte == false) continue;
            this->num1 = num_float;
            std::cout<<"Digite o segundo numero: ";
            std::cin>>n2;
            teste_converte = this->converte(&n2, &num_float);
            if (teste_converte == false) continue;
            this->num2 = num_float;
            if (this->num2 == 0.0)
            {
                std::cout<<"================  DIVISAO POR 0: OPERACAO INVALIDA  ================"<<std::endl;
                this->memoria_limpa = true;
                return this->memoria;
            }
            this->memoria = this->num1 / this->num2;
            std::cout<<"\nResultado: "<<this->num1<<" / "<<this->num2<<" = "<<this->memoria<<std::endl;
        }
    }
    if (this->memoria_limpa == false)
    {
        bool teste_converte = false;
        while (!teste_converte)
        {
            std::cout<<"Digite o numero para dividir com o da memoria: ";
            std::cin>>n1;
            teste_converte = this->converte(&n1, &num_float);
            if (teste_converte == false) continue;
            this->num1 = num_float;
            if (this->num1 == 0.0)
            {
                std::cout<<"================  DIVISAO POR 0: OPERACAO INVALIDA  ================"<<std::endl;
                this->memoria_limpa = false;
                return this->memoria;
            }
            this->num2 = this->memoria;
            this->memoria = this->num2 / this->num1;
            std::cout<<"\nResultado: "<<this->num2<<" / "<<this->num1<<" = "<<this->memoria<<std::endl;
        }
    }
    this->memoria_limpa = false;
    return this->memoria;
}

std::string Calculadora::menu()
{
    std::cout<<"\n\n\n========================================================="<<std::endl;
    std::cout<<"  ============ Valor Memoria Atual: "<<this->memoria<<" ============"<<std::endl;
    std::cout<<"========================================================="<<std::endl;
    std::cout<<"Digite a operacao desejada [ + ] [ - ] [ * ] [ / ] [ C (LIMPA MEMORIA) ] [ S (PARA SAIR) ]"<<std::endl;
    std::string operacao;
    std::cout<<"SUA RESPOSTA: ";
    std::cin>>operacao;
    return operacao;
}

float Calculadora::returnMemoria()
{
    return this->memoria;
}

void Calculadora::limpa_memoria()
{
    this->memoria = 0;
    this->memoria_limpa = true;
}
