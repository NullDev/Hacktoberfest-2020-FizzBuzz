// a fizz buzz in c (first thing I though would work :) )
// Author: @stanmondesir
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char	*ft_strcat(char *s1, char *s2)
{
	int i;
	int j;

	j = 0;
	i = strlen(s1);
	while (s2[j])
	{
		s1[i] = s2[j];
		i++;
		j++;
	}
	s1[i] = '\0';
	return (s1);
}

int main()
{
    char str[12];
    int i;

    i = 1;
    while (i < 100)
    {
        if (i % 3 == 0)
            ft_strcat(str, "Fizz");
        if (i % 5 == 0)
            ft_strcat(str, "Buzz");
        if (!(str[0]))
            printf("%d\n", i);
        else
            printf("%s\n", str);
        str[0] = '\0';
        i++;
    }
}
