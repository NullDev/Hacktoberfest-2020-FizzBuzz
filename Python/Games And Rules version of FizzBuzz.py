def play_game(limit, rules):    
    """ 
    play a specific variant of the FizzBuzz game up to the given limit
    the rules parameter is a list of (number, word) tuples
    e.g. [(3, 'fizz'), (5, 'buzz')]
    """
    for x in range(1, limit+1):
        # select the words where the number is a factor of x
        words = [w for (n,w) in rules if x%n==0]
        # join the words together if there any otherwise answer with the number
        answer = "".join(words) if len(words)>0 else str(x)
        print(answer)

# play FizzBuzz
rules = [(3, 'fizz'), (5, 'buzz')]
play_game(100, rules)

#play FizzBuzzWoof
rules = [(3, 'fizz'), (5, 'buzz'), (7, 'woof')]
play_game(100, rules)
