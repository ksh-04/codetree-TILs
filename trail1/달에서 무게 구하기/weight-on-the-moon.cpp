#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int a = 13;
    double b = 0.165;
    cout << fixed << setprecision(6) << a << " * " << b << " = " << a*b;
    return 0;
}