# A BoyCott-Builtin-Methods implementation of FizzBuzz implementation in Python
# Author: @shivamsn97


fbzlist = [i if i%3 and i%5 else (("fizz" if not i%3 else "") + ("buzz" if not i%5 else "")) for i in range(1,101)]   #The main list is here

def digit_to_character(digit):
    """
    Convert a digit to character. 
    """
    return chr(digit+48)

def int_to_str(num):
    """
    Convert an integer to string. 
    """
    string = ""
    while True:
        digit = int(str(num%10).split(".")[0])      # Converting Float to Integer.
        string = digit_to_character(digit).__add__(string)
        try:
            num = int(str(num).strip()[:-1])            # Removing last digit of integer
        except ValueError:        # When str(num).strip()[:-1] becomes '', ie end. (ValueError: invalid literal for int() with base 10: '')
            break
    return string


def to_string(something): 
    """
    Will be used to map integer and strings from fbzlist so that they all are strings and can be used in join.
    """
    try:
        return int_to_str(something)
    except TypeError:
        return something


Array = "\n".join(map(to_string, fbzlist))    

print(Array)