//A simple C++ code to get FizzBuzz from 1 to any number n instead of just 1 to 100
//Author: @RishabhDevbanshi

#include <iostream>
using namespace std;
 
int main()
{
 int T,num, i=1;;
 cin >> T;
   while(T > 0) {
   cin>>num;
   cout<<"number="<<num<<"T="<<T<<endl;
   i=1;
      while(i<=num){
      if( i%15 == 0) {  //number divisible by 3 and 5 will always be divisible by 15
      cout << "FizzBuzz" << endl; 
      }
      else if(i%5 == 0 ){
      cout << "Buzz" << endl; 
      }
      else if(i%3 == 0) {
      cout << "Fizz" << endl;
      }
       else {
       cout<<i<< endl;
       }
   i++;
   }
 T--;
 }
return 0;
}
