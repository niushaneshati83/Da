#include <iostream>
#include <vector>
using namespace std;

void choclate(vector<int>& n, int k) {
    vector<int> dp(k + 1, 0);
    
    for (int i = 1; i <= k; ++i) {
        for (int x : n) {
            if (i >= x && !dp[i - x]) {
                dp[i] = 1;
                break;
            }
        }
    }
    
    if (dp[k]) {
        cout << "First" << endl;
    } else {
        cout << "Second" << endl;
    }
}

int main() {
    int n_;
    int k;
    cin >> n_ >> k;
    vector<int> arr(n_);
    for (int i = 0; i < n_; ++i) {
        cin >> arr[i];
    }
    
    choclate(arr, k);
    
    return 0;
}
