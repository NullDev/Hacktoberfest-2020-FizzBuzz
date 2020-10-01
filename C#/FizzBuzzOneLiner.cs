// FizzBuzz LINQ One Liner
// Author: @bennybackslash

using System;
using System.Linq;

namespace FizzBuzz
{
    class Fizzy
    {
        static void Main(string[] args)
        {
            Enumerable.Range(1, 100).Select(i =>(i % 3 == 0 && i % 5 == 0) ? "FizzBuzz" : (i % 3 == 0) ? "Fizz" : (i % 5 == 0) ? "Buzz" : i.ToString()).ToList().ForEach(Console.WriteLine);
        }
    }
}
