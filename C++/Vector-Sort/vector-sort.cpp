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
    sort(vect.begin(), vect.end());
    for (int j=0; j<N; j++)
        cout << vect[j] << " ";
    return 0;
}
