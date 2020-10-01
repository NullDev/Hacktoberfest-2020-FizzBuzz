// modular FizzBuzz implementation in CPP 

// Author: @promaroy

#include<bits/stdc++.h>
using namespace std;
string convert_to_string(int i)
{
  string ans="";
  while(i)
  {
    int d=i%10;
    ans=d+'0'+ans;
    i/=10;
  }
  return ans;
}
vector<string> fizzBuzz(int n) {
        vector<string> result;
        for(int i=1;i<=n;i++){
            if(i%3==0 && i%5==0){
                result.push_back("FizzBuzz");
            }
            else if(i%3==0){
                result.push_back("Fizz");
            }
            else if(i%5==0){
                result.push_back("Buzz");
            }
            else
            result.push_back(convert_to_string(i));
        }
        return result;
    }


int main()
{
  int n;
  cout<<"enter the value of n"<<endl;
  cin>>n;
  vector<string> v = fizzBuzz(n);
  for(int i=0;i<v.size();i++)
    cout<<v[i]<<endl;
}
