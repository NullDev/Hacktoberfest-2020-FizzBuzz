// Recursive divide and conquer FizzBuzz, something like a binary search
// Author: @lusmoura

#include <bits/stdc++.h>
using namespace std;

string get_string(int num) {
    string ans = "";
    if (num % 3 == 0) ans += "Fizz";
    if (num % 5 == 0) ans += "Buzz";
    if (ans.empty()) ans = to_string(num);

    return ans;
}

void get_fizzbuzz(int curr_min, int curr_max, vector<string>& fizzbuzz_list) {
    if (curr_min > curr_max) return;
    if (curr_min == curr_max) {
        fizzbuzz_list[curr_min] = get_string(curr_min);
        return;
    }

    int mid = (curr_max+curr_min)/2;
    get_fizzbuzz(mid+1, curr_max, fizzbuzz_list);
    get_fizzbuzz(curr_min, mid, fizzbuzz_list);
}

int main() {
    int n = 100;
    vector<string> fizzbuzz_list(n+1);
    get_fizzbuzz(1, n, fizzbuzz_list);
    
    for (int i = 1; i <= n; i++) {
        cout << i << ": " << fizzbuzz_list[i] << '\n';
    }

    return 0;
}