#include <iostream>
#include <type_traits>

class A {};

int main() {
  std::cout << std::boolalpha;
  std::cout << "is_scalar:" << std::endl;
  std::cout << "int: " << std::is_arithmetic<int>::value << std::endl;
  std::cout << "double: " << std::is_arithmetic<double>::value << std::endl;
  std::cout << "char: " << std::is_arithmetic<char>::value << std::endl;

  return 0;
}