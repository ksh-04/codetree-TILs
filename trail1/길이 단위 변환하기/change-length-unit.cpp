#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double ft = 30.48;
    double mi = 160934;
    
    cout << fixed << setprecision(1) << "9.2ft = " << 9.2 * ft << "cm" << endl;
    cout << fixed << setprecision(1) << "1.3mi = " << 1.3 * mi << "cm";
    return 0;
}