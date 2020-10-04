using System;

class FizzBuzz
{
    public static void Main(string[] args)
    {
        for (int i = 1; i <= 100; i++)
        {
            string fizzBuzz = "";

            if(IsDivisible(i, 3)) fizzBuzz += "Fizz";

            if (IsDivisible(i, 5)) fizzBuzz += "Buzz";
            
            Console.WriteLine((fizzBuzz != "") ? fizzBuzz : i.ToString()); 
        }
    }

    private static bool IsDivisible(int number, int _divisor)
    {
        int divisor = _divisor;

        while (divisor < number) divisor += _divisor;

        return divisor == number;
    }
}