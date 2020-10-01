// A little FizzBuzz in C, with just one printf,
// with a const char*.
// Author: @Mel-louie

#include <stdio.h>

int		main() {
	int			i = 0;
	const char	*str;

	while (i++ < 100) {
		int Fizz = (i % 3 == 0) ? 1 : 0;
		int Buzz = (i % 5 == 0) ? 1 : 0;

		str =	(Fizz && Buzz) ? "FizzBuzz\n" :
				Fizz ? "Fizz\n" :
				Buzz ? "Buzz\n" :
				"%d\n";
		
		printf(str, i);
	}
	return (0);
}