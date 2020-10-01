# FizzBuzz using binary numbers
# Author @Nadiminty Kaundinya
def fizzbuzz(n):
    for i in range(1, n+1):
        # Getting the binary representation of i and reversing it
        bin_i = list(map(int, list(bin(i)[2:])))[::-1]
        # Counting number of set bits in binary representation of i at odd places
        odd_set_bits_count = bin_i[::2].count(1)
        # Counting number of set bits in binary representation of i at even places
        even_set_bits_count = bin_i[1::2].count(1)
        # If the absolute difference of above two variables modulo 3 is 0, then it is multiple of 3
        is_multiple_of_3 = (
            abs(odd_set_bits_count - even_set_bits_count) % 3) == 0

        # These are the offset values of digit positions modulo 5
        multiple_5_offset = [1, 2, 4, 3]
        offset_length = len(multiple_5_offset)

        # If the sum modulo 5 is 0, then it is multiple of 5
        is_multiple_of_5 = (sum([multiple_5_offset[j % offset_length]
                                 * bin_i[j] for j in range(len(bin_i))]) % 5) == 0

        # Comparing boolean values to print the necessary value
        if is_multiple_of_5:
            if is_multiple_of_3:
                print("FizzBuzz")
            else:
                print("Buzz")
        elif is_multiple_of_3:
            print("Fizz")
        else:
            print(i)
