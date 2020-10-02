// Fuzz Buzz
// Author: Sewern Kaminski

#include <array>
#include <iostream>
#include <numeric>

using namespace std;

int main() {
    std::cout << "Fizz buzz" << std::endl;

    auto print = []( int v ) {
        auto f = !(v % 3);
        auto b = !(v % 5);
        cout << ( f && b ? "fizzbuzz" :
                       f ? "fizz" :
                       b ? "buzz" : to_string( v )) << endl;
    };

    std::array<int,100> tab;

    std::iota ( tab.begin(), tab.end(), 1 );

    std::for_each ( tab.begin(), tab.end(), print );
}
