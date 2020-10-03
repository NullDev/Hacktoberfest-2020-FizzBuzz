#include <iostream>

using namespace std;
class fizzbuzz
{
    int a,i;
public:
    fizzbuzz()
    {
        a=0;
        i=0;
    }
    void input()
    {
        cout<<"enter value of a"<<endl;
        cin>>a;
    }
    void compute()
    {
        for(i=1;i<=a;i++)
        {
            if(i%15==0)
                cout<<"fizzbuzz"<<endl;
            else if(i%3==0)
                cout<<"fizz"<<endl;
            else if(i%5==0)
                cout<<"buzz"<<endl;
            else
            {
                cout<<i<<endl;
            }
        }
    }
};

int main()
{
    fizzbuzz ob;
    ob.input();
    ob.compute();
    return 0;
}
