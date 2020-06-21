#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    set<int>s;
    int count;
    cin >> count;
    for (int i=0; i<count; i++){
        int type, query;
        cin >> type >> query;
        if (type == 1){
            s.insert(query);
        }
        else if (type == 2) {
            s.erase(query);
        }
        else if (type == 3) {
            cout << (s.find(query) == s.end() ? "No" : "Yes") << endl;
        };
    }
    return 0;
}