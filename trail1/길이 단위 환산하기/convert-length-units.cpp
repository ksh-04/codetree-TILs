#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double N;
    cin >> N;
    cout << fixed << setprecision(1) << 30.48 * N;
    
    return 0;
}