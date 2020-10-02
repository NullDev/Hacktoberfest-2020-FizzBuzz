#include <bits/stdc++.h>
using namespace std;

int main() {
	
	string s[101];
    	for(int i=1;i<=100;i++)
	{
		s[i]=to_string(i);
	}
	for(int i=3;i<=100;i+=3)
	{
		s[i]="Fizz";
		
	}
		for(int i=5;i<=100;i+=5)
	{
		s[i]="Buzz";
		
	}
		for(int i=15;i<=100;i+=15)
	{
		s[i]="FizzBuzz";
		
	}
		for(int i=1;i<=100;i++)
	{
		cout<<s[i]<<" ";
	}
	return 0;
}