#include <iostream>
#include <vector>
#include <sstream>
using namespace std;
int calculate_output(int n, const vector<int>& array) {
    int number_of_ones = 0;
    for (int num : array) {
        if (num == 1) {
            number_of_ones++;
        }
    }
    return n - (number_of_ones / 2);
}
vector<int> read_integers() {
    vector<int> array;
    string line;
    getline(cin, line);
    istringstream iss(line);
    int temp;
    while (iss >> temp) {
        array.push_back(temp);
    }
    return array;
}

int main() {
    string line1;
    getline(cin, line1);
    int t = stoi(line1);

    vector<pair<int, vector<int>>> result;

    for (int i = 0; i < t; ++i) {
        string line2;
        getline(cin, line2);
        int n = stoi(line2);

        vector<int> array = read_integers();
        result.push_back(make_pair(n, array));
    }

    for (const auto& p : result) {
        cout << calculate_output(p.first, p.second) << endl;
    }

    return 0;
}