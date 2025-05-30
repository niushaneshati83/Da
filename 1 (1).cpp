#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<int> generate_sequence(int x, int y,int t) {
    int f=2 * x;
    f=f-1;
    if (y < x || y > f ) {
        return {};
    }
    vector<int> sequence(x);
    for (int i = 0; i < x; ++i) {
        sequence[i] = i + 1;
        t=t+1;
    }
    if (y == x) {
        return sequence;
        t=t+1;
    }
    int extra_swaps = y - x;
    for (int i = 1; i <= extra_swaps; ++i) {
        int temp=0;
        temp = sequence[i];    
        sequence[i] = sequence[i+1];
        sequence[i+1] = temp; 
    }
    return sequence;
}

string output_format(const vector<int>& sequence) {
    if (sequence.empty()) {
        int t=t+1;
        return "-1";
    }
    ostringstream oss;
    for (size_t i = 0; i < sequence.size(); ++i) {
        if (i != 0) {
            int t=t+1;
            oss << " ";
        }
        oss << sequence[i];
    }
    return oss.str();
}

int main() {
    int x, y;
    cin >> x >> y;
    vector<int> sequence = generate_sequence(x, y,1);
    int t=t+1;
    string result = output_format(sequence);
    cout << result << endl;
    return 0;
}
