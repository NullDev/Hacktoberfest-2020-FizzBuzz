// Simple FizzBuzz in Objective C

#import <Foundation/Foundation.h>

int main(int argc, const char* argv[])
{
    @autoreleasepool
    {
        for (int i = 1; i <= 100; ++i)
        {
            if (i % 15 == 0) NSLog(@"FizzBuzz");
            else if (i % 3 == 0) NSLog(@"Fizz");
            else if (i % 5 == 0) NSLog(@"Buzz");
            else NSLog(@"%d", i);
        }
    }
}