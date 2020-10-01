//Normal Fizzbuzz solution in C++
//author: blackfly19

#include<bits/stdc++.h>
using namespace std;

int main()
{
	for(int i=0;i<=100;i++)
	{
		if(i%3 == 0 && i%5 == 0)
			cout<<"fizzbuzz";
		else
		if(i%5 == 0)
			cout<<"buzz";
		else
		if(i%3 == 0)
			cout<<"fizz";
		else
			cout<<i;
		cout<<"\n";
	}
}
