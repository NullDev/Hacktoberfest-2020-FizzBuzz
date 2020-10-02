#include<bits/stdc++.h>
using namespace std;

typedef struct Fizz{
	string a;
	string b;
	string c;
}Fizz;

int main()
{
	cout << "+----------------------------------------------------------+" << endl;
	cout << "Welcome to create FizzBuzz" << endl;
	long n;
	cout << "Enter the number : ";
	cin >> n;
	Fizz *names = new Fizz;
	names->a = "Fizz";
	names->b = "Buzz";
	names->c = "FizzBuzz";
	for(int i=1;i<=n;i++){
		if(i%3==0 && i%5 == 0)
			cout << names->c;
		else if(i%5==0)
			cout << names->b;
		else if(i%3==0)
			cout << names->a;
		else
			cout << i;
		cout <<endl;
	}
	return 0;
}