#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, q;
    cin >> n >> q;
    vector <vector<int>> a(n);
    for (int i=0; i<n; i++)
    {
        int inp;
        cin >> inp;
        a[i].resize(inp);
        for (int j = 0; j < inp; j++) {
            cin >> a[i][j];
        }
    }   

    for (int queries=0; queries<q; queries++)
    {
        int i,j;
        cin >> i >> j;
        cout << a[i][j] << endl;
    }
    return 0;
}