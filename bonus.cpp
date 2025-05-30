#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    int w = 4;
    int n;
    cin >> n;
    vector<vector<int>> graph(n, vector<int>(n));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> graph[i][j];
        }
    }

    vector<int> vertex;
    for (int i = 0; i < w; i++) {
        if (i != 0 && w == 4) {
            vertex.push_back(i);
        }
    }

    int javab = INT_MAX;
    do {
        int x=0;
        int path = 0;
        int k = 0;
        for (int i = 0; i < vertex.size(); i++) {
            int q=vertex[i];
            path = path + graph[k][q];
            k = vertex[i];
            x= x+1;
        }
        path = path + graph[k][0];
        if (int(javab) < int(path)){
            javab =javab;
        }
        else{
            javab = int(path);
        }
    } while (next_permutation(vertex.begin(), vertex.end()));

    cout << javab << endl;
    return 0;
}
