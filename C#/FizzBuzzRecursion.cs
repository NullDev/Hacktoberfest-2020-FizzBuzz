// FizzBuzz using recursion method
// Author: @justinushermawan

using System;

namespace FizzBuzz
{
    class Main
    {
        static void Main(string[] args)
        {
            FizzBuzz(1);
        }

        private static void FizzBuzz(int iter)
        {
            string str = "";

            if (iter % 3 == 0) str += " Fizz";
            if (iter % 5 == 0) str += " Buzz";

            Console.Write(str == "" ? (" " + iter) : str);

            if (iter >= 100) return;

            FizzBuzz(++iter);
        }
    }
}
