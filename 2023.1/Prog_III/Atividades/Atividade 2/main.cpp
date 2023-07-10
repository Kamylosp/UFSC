/*  Atividade 2 de Programação III
    Alunos: Kamylo Serafim Porto e Pedro Augusto Vargas Dantas
    Turma: Sexta-feira */

#include <iostream>
#include <string.h>

using namespace std;

class Person {
    private:
    string name;
    string birthDate;
    string sex;

    public:
    Person (string, string, string);

    string getName ();
    string getBirthDate ();
    string getSex ();
};

class University {
    private:
    string Uname;

    public:
    University (string);

    string getUname();
};

class Student : public Person, public University{
    private:
    string department;

    public:
    Student (string, string, string, string, string);

    string getDepartment();
};

class Teacher : public Person, public University {
    private:
    string department;
    string course;

    public:
    Teacher (string, string, string, string, string, string);

    string getDepartment();
    string getCourse ();
};

class TeachingAssistant : public Student, public Teacher{
    public:   
    TeachingAssistant(string, string, string, string, string, string, string);

};


int main () {
    cout<<"--- Student ---"<<endl;
    Student aluno("Paulo", "17/09/1990", "Male", "UFSC", "EMB");
    cout<<aluno.getName()<<endl;
    cout<<aluno.getBirthDate()<<endl;
    cout<<aluno.getSex()<<endl;
    cout<<aluno.getUname()<<endl;
    cout<<aluno.getDepartment()<<endl;

    cout<<"--- Teacher ---"<<endl;
    Teacher professor("Rafael", "09/12/1970", "Male", "UFSC", "EMB", "Prog III");
    cout<<professor.getName()<<endl;
    cout<<professor.getBirthDate()<<endl;
    cout<<professor.getSex()<<endl;
    cout<<professor.getUname()<<endl;
    cout<<professor.getDepartment()<<endl;
    cout<<professor.getCourse()<<endl;

    cout<<"--- Teaching Assistant ---"<<endl;
    TeachingAssistant assistente("Samira", "18/05/1990", "Female", "UFSC", "EMB", "EE", "Prog III");
    cout<<assistente.Student::getName()<<endl;
    cout<<assistente.Student::getBirthDate()<<endl;
    cout<<assistente.Student::getSex()<<endl;
    cout<<assistente.Student::getUname()<<endl;
    
    cout<<"Student's department: ";
    cout<<assistente.Student::getDepartment()<<endl;
    
    cout<<"Teaching department: ";
    cout<<assistente.Teacher::getDepartment()<<endl;
    
    cout<<assistente.getCourse()<<endl;
    
}


// Classe Person
Person::Person (string nome, string data, string sexo){
    name = nome;
    birthDate = data;
    sex = sexo;
}

string Person::getName (){
    return name;
}

string Person::getBirthDate (){
    return birthDate;
}

string Person::getSex (){
    return sex;
}


// Class University
University::University (string universidade){
    Uname = universidade;
}

string University::getUname (){
    return Uname;
}

// Classe Student
Student::Student (string nome, string data, string sexo, string universidade, string depart)
: Person (nome, data, sexo), University(universidade) {
    department = depart;
}

string Student::getDepartment (){
    return department;
}

// Classe Teacher
Teacher::Teacher (string nome, string data, string sexo, string universidade, string depart, string curso) 
: Person (nome, data, sexo), University(universidade) {
    department = depart;
    course = curso;
}

string Teacher::getDepartment(){
    return department;
}

string Teacher::getCourse (){
    return course;
}

// Classe TeachingAssistant
TeachingAssistant::TeachingAssistant (string nome, string data, string sexo, string universidade, string stu_depart, string tea_depart, string curso) :
Student(nome, data, sexo, universidade, stu_depart), Teacher (nome, data, sexo, universidade, tea_depart, curso) {}
