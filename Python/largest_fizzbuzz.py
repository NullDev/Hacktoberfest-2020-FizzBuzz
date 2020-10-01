def largest(max) -> int:
    """
    Returns the highest number fizzbuzz wihtin the max limit, if there is none, return -1
    """
    while max >0:
        if max % 3 == 0 and max % 5 == 0:
            return max
        max-= 1
    return -1

