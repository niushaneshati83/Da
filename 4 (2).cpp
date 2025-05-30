#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n_, x;
    cin >> n_ >> x;
    
    vector<int> arr(n_);
    for (int i = 0; i < n_; ++i) {
        cin >> arr[i];
    }
    
    int sum_arr = 0;
    for (int num : arr) {
        sum_arr += num;
    }
    
    vector<vector<long long>> dp(sum_arr + 1, vector<long long>(n_ + 1, 0));
    dp[0][0] = 1;
    
    int a = sum_arr;
    for (int num : arr) {
        for (int s = a; s >= num; --s) {
            for (int k = n_; k >= 1; --k) {
                dp[s][k] += dp[s - num][k - 1];
            }
        }
    }
    
    long long result = 0;
    for (int j = 1; j <= n_; ++j) {
        int sum_akhar = x * j;
        if (sum_akhar <= sum_arr) {
            result += dp[sum_akhar][j];
        }
    }
    
    cout << result << endl;
    
    return 0;
}
