//This one helps to decrease the time complexity by using sieve like approach
//Author: @RishabhDevbanshi

#include <bits/stdc++.h> 
using namespace std;
#define ll long long 

int main() {
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n;
	cin>>n;
	bool isDone[n+1];
	memset(isDone,false,sizeof(isDone));
	vector<int> v(n+1);
	for(int i=1;i<=n;i++)
	{
	    if(i%15 == 0 and (v[i]==3 or v[i]==5))
	    {
	        for(int j=i;j<=n;j+=i)
	        {
	            v[j]=15;
	        }
	    }
	    else if(i%5==0 and isDone[i]==false)
	    {
	        for(int j=i;j<=n;j+=i)
	        {
	            v[j]=5;
	            isDone[j]=true;
	        }
	    }
	    else if(i%3==0 and isDone[i]==false)
	    {
	        for(int j=i;j<=n;j+=i)
	        {
	            v[j]=3;
	            isDone[j]=true;
	            
	        }
	    }
	    else if(isDone[i]==false)
	    {
	        v[i]=i;
	        isDone[i]=true;
	    }
	}
	
	for(int i=1;i<=n;i++) 
	{
	    if(v[i]==3) cout<<"Fizz ";
	    else if(v[i]==5) cout<<"Buzz ";
	    else if(v[i]==15) cout<<"FizzBuzz ";
	    else cout<<i<<" ";
	}
	
	
	
	return 0;
}
