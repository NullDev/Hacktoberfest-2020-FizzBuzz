// Simple version of FizzBuzz in bash
// Author: @jmmille

using System;

namespace FizzBuzz
{
    class Program
    {
        static void Main(string[] args)
        {
            for (int i = 0; i < 101; i++)
            {
                if (i % 3 == 0 && i % 5 == 0)
                {
                    Console.WriteLine("fizzbuzz");
                    continue;
                } else if (i % 3 == 0){
                    Console.WriteLine("fizz");
                    continue;
                } else if (i % 5 == 0)
                {
                    Console.WriteLine("buzz");
                    continue;
                }
                Console.WriteLine(i);
            } 
        }
    }
}
