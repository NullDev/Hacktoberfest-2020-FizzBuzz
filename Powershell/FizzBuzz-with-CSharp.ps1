$randomID = Get-Random
$code = @"
using System;
namespace FizzBuzz
{
    public class FizzBuzz$randomID
    {
        public static void Main(string[] args)
        {
            for (int i = 1; i <= 100; i++)
            {
                if (i % 3 == 0 && i % 5== 0)
                {
                    Console.WriteLine("FizzBuzz");
                }
                else if (i % 3 == 0)
                {
                    Console.WriteLine("Fizz");
                }
                else if (i % 5 == 0)
                {
                    Console.WriteLine("Buzz");
                }
                else
                {
                    Console.Write(i + "\n");
                }
            }
        }
    }
}
"@

Add-Type -TypeDefinition $code -Language CSharp
iex "[FizzBuzz.FizzBuzz$randomID]::Main(`"`")"