// FizzBuzz Problem using C++
// Author: @gourab337

#include<bits/stdc++.h>

using namespace std;

int main(){

 for (int i=1; i<101; i++){
     if(i%3 == 0)
         cout<<"FIZZ ";
     if(i%5 == 0)
      cout<<"BUZZ ";
     if((i%3)*(i%5))    // if (i%3) && (i%5) !=0, then only the if case gets executed
        cout<<i<<" ";
     
     cout<<",";
}

}