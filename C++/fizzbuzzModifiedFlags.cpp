/*Modified FizzBuzz-
Prints numbers from 1-100 AND
Prints fizz is the number is divisble by 3 and/or includes a 3
Prints buzz if the number is divisble by 5 and/or contains a 5
Prints fizzbuzz is the number meets both of those conditions
Solution has a lot of flags and if statements, I thought this would be a unique solution with a twist to the "normal" fizzbuzz using C++. 
Author: @yashgajaria
*/ 


#include <iostream>
using namespace::std;

int main() {
  int ones=0;
  bool caseA= false;
  bool caseB= false;

  //Looping through all numbers from 1-100
  for (int i=1; i<101; i++){
    //Determining what number is in the ones column to check if there is a 3 or 5
      ones=i%10;
      if (i%3==0|| ones==3 || i-ones==30){
          caseA= true;
      }
      if (i%5==0 || ones==5|| i-ones==50){
          caseB= true;
      }
      
      //Print number and statements as needed
      if (caseA && !caseB){
          cout<<i<<"fizz";
          }
      else if (!caseA && caseB){
          cout<<i<<"buzz";
          }
      else if (caseA && caseB){
          cout<<i<< "fizzbuzz";
          }
    else {
        cout<<i;
      }
    //Reset flags and move to next line
    cout<<endl;
    caseA=false;
    caseB=false;
  }

}
