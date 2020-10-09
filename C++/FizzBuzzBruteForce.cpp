#include <bits/stdc++.h>
using namespace std;

//Check if a solution is valid
bool checkSol(vector<string> &sol) {
    for (int i = 1; i <= 15; i++) {
        if (sol[i-1] == "FizzBuzz" && i % 15 != 0) return false;
        if (sol[i-1] == "Fizz" && i % 3 != 0) return false;
        if (sol[i-1] == "Buzz" && i % 5 != 0) return false;
    }

    return true;
}

int main() {
    vector<string> sol;
    
    //Add the correct numbers of FizzBuzz, Fizz, Buzz, and num as a placeholder for number
    for (int i = 0; i < 1; i++) sol.push_back("FizzBuzz");
    for (int i = 0; i < 4; i++) sol.push_back("Fizz");
    for (int i = 0; i < 2; i++) sol.push_back("Buzz");
    for (int i = 0; i < 8; i++) sol.push_back("num");

    //Sort it to use next_permutation
    sort(sol.begin(), sol.end());

    //Go through all the permutations
    do {
        //If valid solution, output vector and exit
        if (checkSol(sol)) {
            for (int i = 1; i <= 15; i++) {
                if (sol[i-1] == "num") cout << i << endl;
                else cout << sol[i-1] << endl;
            }

            return 0;
        }
    }
    while (next_permutation(sol.begin(), sol.end()));

}
