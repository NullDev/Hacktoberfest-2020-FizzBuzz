#include <bits/stdc++.h>
using namespace std;

void reverseRecursiveFizzBuzz(int n) {
    if(n == 0)
        return;
    else if(n % 3 == 0 && n % 5 == 0)
        cout << "FizzBuzz" << endl;
    else if(n % 3 == 0)
        cout << "Fizz" << endl;
    else if(n % 5 == 0)
        cout << "Buzz" << endl;
    else
        cout << n << endl;
    fizzbuzz(n - 1);
}

int main(int argc, char const *argv[]) {
    int n;
    cin >> n;
    fizzbuzz(n);
    
    return 0;
}
