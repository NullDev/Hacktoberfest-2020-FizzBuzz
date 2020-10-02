// an example in how not to write code. but it works.
// Author: @s0la1337

#include <iostream>
#include <string>

class Base
{
public:
    Base(const int a)
        : result(std::to_string(a))
    { }
    ~Base() = default;
    
    virtual std::string solve()
    {
        return result;
    }
    
protected:
    std::string result;
};

class Fizz : public Base
{
public:
    Fizz(const int a)
        : Base(a)
    { 
        result = (!(std::stoi(result) % 3)) ? "Fizz" : Base::solve();
    }
};

class Buzz : public Base
{
public:
    Buzz(const int counter)
        : Base(counter)
    {
        result = (!(std::stoi(result) % 5)) ? "Buzz" : Base::solve();
    }
    
};

class Fizzbuzz : public Fizz, public Buzz
{
public:
    Fizzbuzz(const int counter)
        : Fizz(counter)
        , Buzz(counter)
        , original(std::to_string(counter))
    { }
    
    std::string solve() override
    {
        std::string res{Fizz::result + Buzz::result};
        if(res.size() > 7)
            return res;
        else if(Fizz::result != original)
            return Fizz::result;
        else if(Buzz::result != original)
            return Buzz::result;
            
        return original;
    }
private:
    std::string original;
};

int main()
{
    for(auto i = 1; i <= 100; ++i)
    {
        Fizzbuzz fb{i};
        std::cout << fb.solve() << '\n';
    }
}
