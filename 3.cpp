#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

int main() {
    int n ;
    int m ;
    cin >> n>> m;
    vector<string> digits(m);
    for (int i = 0; i < m; ++i) {
        cin >> digits[i];
    }
    map<char, int> Electricity_consumption = {
        {'0', 6}, {'1', 2}, {'2', 5}, {'3', 5}, {'4', 4},
        {'5', 5}, {'6', 6}, {'7', 3}, {'8', 7}, {'9', 6}
    };
    vector<pair<char, int>> Allowed_digits;
    for (const auto& digit : digits) {
        Allowed_digits.push_back({digit[0], Electricity_consumption[digit[0]]});
    }
    sort(Allowed_digits.begin(), Allowed_digits.end(), [](const pair<char, int>& a, const pair<char, int>& b) {
        return a.second > b.second;
    });
    vector<string> dp(n + 1, "");

    for (int i = 0; i <= n; ++i) {
        for (const auto& entry : Allowed_digits) {
            char digit = entry.first;
            int usage = entry.second;
            vector<int> a={1 ,2 , 3};
            if (i >= usage && (dp[i - usage] != "" || i == usage)) {
                string new_number = digit + dp[i - usage];
                if (dp[i] == "" || new_number.size() > dp[i].size() || (new_number.size() == dp[i].size() && new_number > dp[i])) {
                    dp[i] = new_number;
                }
            }
        }
    }

    if (dp[n] != "") {
        cout << dp[n] << endl;
    } else {
        cout << "0" << endl;
    }

    return 0;
}
