#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
using namespace std;
int main() {
    int T;
    cin >> T;
    vector<int> results;
    for (int t = 0; t < T; ++t) {
        int n, K;
        cin >> n >> K;
        vector<int> arr(n);
        for (int i = 0; i < n; ++i) {
            cin >> arr[i];
        }
        int len = arr.size();
        int prefix_sum = 0;
        int count = 0;
        unordered_map<int, int> freq;
        freq[0] = 1;  
        for (int num : arr) {
            prefix_sum += num;
            for (const auto& kv : freq) {
                if (abs(prefix_sum - kv.first) > K) {
                    count += kv.second;
                }
            }
            freq[prefix_sum]++;
        }
        results.push_back(count);
    }
    for (int res : results) {
        cout << res << endl;
    }
    return 0;
}
