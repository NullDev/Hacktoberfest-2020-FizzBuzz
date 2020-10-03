// Segment tree solution for FizzBuzz
// *Storing two variables for every node so we
// can check if it is a multiple or not*
// Author: @nikolatechie

#include <iostream>
using namespace std;

struct Node {
    string out; // message
    int cnt = 0; // count multiples of 3 and 5

    void updateMessage(int &multiple, bool isMultiple) {
        if (this->cnt == 0)
            this->out = to_string(multiple); // output isn't a multiple of 3 nor 5
        else if (this->cnt == 1) {
            if (isMultiple)
                this->out = ((multiple == 3) ? "Fizz":"Buzz"); // multiple of one number
        }
        else this->out = "FizzBuzz"; // multiple of both 3 and 5
    }
};

Node st[410];

void addMultiple(int node, int l, int r, int multiple) {
    if (l == r) {
        if (l % multiple == 0) {
            ++st[node].cnt;
            st[node].updateMessage(multiple, 1);
        }
        else st[node].updateMessage(l, 0);

        return;
    }

    int m = (l+r)>>1;
    addMultiple(node<<1, l, m, multiple); // left half
    addMultiple((node<<1)|1, m+1, r, multiple); // right half
}

void printSolution(int node, int l, int r) {
    if (l == r)
        cout << st[node].out << ' ';
    else {
        int m = (l+r)>>1;
        printSolution(node<<1, l, m);
        printSolution((node<<1)|1, m+1, r);
    }

    if (l == 1 && r == 100)
        cout << '\n';
}

int main() {
    ios_base::sync_with_stdio(0);


    addMultiple(1, 1, 100, 3);
    addMultiple(1, 1, 100, 5);
    printSolution(1, 1, 100);



    return 0;
}