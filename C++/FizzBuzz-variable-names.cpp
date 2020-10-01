#include <iostream>
// This macro will help us to print the name of the variable
#define printVariableName(var) cout << (#var) << endl
using namespace std;
void fizzbuzz(int n)
{
    // We will use the macro defined above to print the name of the variables declared below
    int Fizz = 3, Buzz = 5, FizzBuzz = 15;
    int i = 1;
    while (i <= n)
    {
        if (i % 15 == 0)
        {
            printVariableName(FizzBuzz);
        }
        else if (i % 3 == 0)
        {
            printVariableName(Fizz);
        }
        else if (i % 5 == 0)
        {
            printVariableName(Buzz);
        }
        else
        {
            cout << i << "\n";
        }
        i++;
    }
}

int main()
{
    cout << "Enter the value of n:";
    int n;
    cin >> n;
    fizzbuzz(n);
    return 0;
}