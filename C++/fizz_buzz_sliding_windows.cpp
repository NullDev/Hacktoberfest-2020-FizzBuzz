/******************************************************************************

                              This Code is developed by Sombit 
                    This program uses Sliding Windows Algorithm and
                modulo operator for finding fizz, buzz, fizzbuzz, the 
            python implementation is available in the Python folder of 
                                   this repository.

*******************************************************************************/

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

struct window {
    int start,end;
};

int main()
{
    struct window slide_3;
    struct window slide_5;
    set <int> fizz;
    set <int> buzz;
    set <int> fizz_buzz;
    slide_3.start = 1; slide_3.end = 3;
    slide_5.start = 1; slide_5.end = 5;
    while (slide_3.end < 100 && slide_5.end < 100) {
        if (slide_3.end == slide_5.end)
            fizz_buzz.insert(slide_3.end);
        else {
            fizz.insert(slide_3.end);
            if (slide_5.end % 15 != 0)
                buzz.insert(slide_5.end);
        }
        slide_3.start += 3; slide_3.end += 3;
        if (slide_3.end > slide_5.end) {
            slide_5.start += 5; slide_5.end += 5;
        }
    }
    cout << "The Fizz numbers" << endl;
    for (auto x: fizz)
        cout << x << " ";
    cout << "\nThe Buzz numbers" << endl;
    for (auto x: buzz)
        cout << x << " ";
    cout << "\nThe Fizz Buzz numbers" << endl;
    for (auto x: fizz_buzz)
        cout << x << " ";
    return 0;
}
