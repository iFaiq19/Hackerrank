#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    vector <int> vect;
    int N, integers;
    cin >> N;
    for (int i=0; i<N; i++)
    {
        cin >> integers;
        vect.push_back(integers);
    }
    int a, b, c;
    cin >> a; cin >> b; cin >> c;
    vect.erase(vect.begin()+(a-1));
    vect.erase(vect.begin()+(b-1),vect.begin()+(c-1));
    cout << vect.size() << endl;
    for (int i=0; i<vect.size(); i++)
        cout << vect[i] << " ";
    return 0;
}
