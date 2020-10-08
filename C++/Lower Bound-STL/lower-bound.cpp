#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int N, num;
    cin >> N;
    vector<int> vect;
    for (int i=0; i< N; i++)
    {
        cin >> num;
        vect.push_back(num);
    }
    int n, value;
    cin >> n;
    for (int j=0; j<n; j++)
    {
        cin >> value;
        vector<int>::iterator low;
        low=lower_bound(vect.begin(), vect.end(), value);
        if (vect[low-vect.begin()] == value)
            cout << "Yes " << (low - vect.begin()+1) << endl;
        else
           cout << "No " << (low - vect.begin()+1) << endl;
    }
    return 0;
}
