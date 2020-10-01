BEGIN {
    printf "Enter value of n: ";
    # Reading value entered by user as string 
    getline n < "-";
    # Converting the type of n from string to int
    n = n + 0
    for (i = 1; i <= n; ++i) {
        if(i % 15 == 0) print "FizzBuzz";
        else if (i % 5 == 0) print "Buzz";
        else if (i % 3 == 0) print "Fizz";
        else print i; 
    }
}