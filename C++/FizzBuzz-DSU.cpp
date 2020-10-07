// The solution follows an approach for making 3 disjoint sets(divisible by 15,divisible by 3, divisible by 5), the tree structure
// in which a number is present will contain the string which it is expected to print.
// Author : yadavnaman
#include <bits/stdc++.h>
#define rep(i,a,b) for(int i = a; i <b; ++i)
using namespace std;
const int maxn = 104;
int par[maxn];
int sz[maxn];
string res[maxn];
void make_set(int n) {
    for(int a=1;a<=n;a++){
        par[a]=a;
        sz[a]=1;
        if(a <= 100){
        	res[a] = to_string(a);
        }
        if(a == 101){
        	res[a] = "Fizz";
        }
        if(a == 102){
        	res[a] = "Buzz";
        }
        if(a == 103){
        	res[a] = "FizzBuzz";
        }
    }
}

int find_set(int v) {
    if (v == par[v])
        return v;
    return par[v] = find_set(par[v]);
}

void union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (sz[a] < sz[b])
            swap(a, b);
        par[b] = a;
        sz[a] += sz[b];
    }
}

void FizzBuzz() {
	make_set(103);
	int i = 3;
	i = 15;
	for(; i<=100; i+=15){
		union_sets(103,i);
	}
	i = 3;
	for(; i<=100; i+=3){
		if(i == find_set(i)){
			union_sets(101,i);
		}
	}
	i = 5;
	for(; i<=100; i+=5){
		if(i == find_set(i)){
			union_sets(102,i);
		}
	}
	

	rep(i,1,101){
		cout << res[find_set(i)] << " ";
	}

}

int32_t main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	FizzBuzz();
}
