/* This Program uses C++ STL and #define macro processor to write the program. We can use it to code very fast
in programing contest have made a template already;*/
// Anuranjan Srivastava (Codersaty)

#include<bits/stdc++.h>
#include<iostream>
#include<map>
#define mis map<int,string>
#define mi map<int,int>
#define loop(i,n) for(int i=1;i<=n;i++)
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    mi m;
    loop(i,100)
    {
        if(i%3==0 && i%5==0)
        m[i]=-2;
        else if(i%3==0)
        m[i]=-1;
        else if(i%5==0)
        m[i]=0;
        else
        m[i]=i;
    }
	cout<<endl;
	
    loop(i,100)
    {
        if(m[i]==-2)
            cout<<"FizzBuzz";
        else if(m[i]==-1)
            cout<<"Fizz";
        else  if(m[i]==0)
            cout<<"Buzz";
        else
            cout<<" "<<m[i]<<" ";
    }
}


