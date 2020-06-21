#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

void max_of_four(int a, int b, int c, int d) {
    int an1 = fmax(a, b);
    int an2 = fmax(c, d);
    cout << fmax(an1, an2);
}

int main() {
    int a, b, c, d;
    cin >> a; cin >> b; cin >> c; cin >> d;
    max_of_four(a, b, c, d);
    
    return 0;
}
