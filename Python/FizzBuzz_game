# Author : Utsav Ramchandra Khatu
# FizzBuzz Game Just like Rock-Paper-Scissors but better than it
"""
    Common instruction :
        1. It is a two player Game
        2. It is fairly simple Game , where each Player enters a number
        3. Game consists of differents levels/rounds
        4. Game is won by the player who first earns 5 points
        5. Winning a round gives the player 1 point
        6. If the entered number is divisible by 3 and 5 the number is called FizzBuzz
        7. If the entered number is divisible by 3 the number is called Fizz
        8. If the entered number is divisible by 5 the number is called Buzz
        9. If the entered number is not divisible by 3 nor 5 the number is called None

    Rules for the Game :
        1. FizzBuzz beats both Fizz and Buzz
        2. None beats FizzBuzz
        3. Fizz and buss both beats None
        4. Fizz beats Buzz if and only if the player who chose Fizz has less point than the another player who chose Buzz
        5. Buzz beats Fizz if and only if the player who chose Buzz has less point than the another player who chose Fizz
        6. If all the above rules fails the round ties

    Diagramatic Representation of the Rules :

    ? : denotes beats
                             Fizz Buzz
                             /   ?   \
                            /    |    \
                           ?     |     ?
                         Fizz    |    Buzz
                          |\     |     /|
                          | \    |    / |
                          |  ?   |   ?  |
                          |    None     |
                          |_____________|
                                |
                                |
                            ____|____
                           /    |    \
                          /     |     \
                         /      |      \
                    if p1>p2 if p1=p2 if p1<p2
                      p2+=1    tie      p1+=1
"""

"""
    0 : FizzBuzz
    1 : Fizz
    2 : Buzz
    3 : None
"""

def fizzbuzz(n) :
    if n%15 == 0 :
        return 0
    elif n%3 == 0 :
        return 1
    elif n%5 == 0 :
        return 2
    else :
        return 3


p1,p2 = 0,0
x = 0
while max(p1,p2) != 5 :
    x+=1
    print(f"Round {x}")
    while True :
        print(f"Enter the number player 1 : ",end ="")
        np1 = int(input())
        if np1 > 0 :
            break
        print(f"No is Invalid!! Please try again")
    while True :
        print(f"Enter the number player 2 : ",end ="")
        np2 = int(input())
        if np2 > 0 :
            break
        print(f"No is Invalid!! Please try again")
    np1 = fizzbuzz(np1)
    np2 = fizzbuzz(np2)
    if np1 == 0 :
        if (np2 == 1 or np2 == 2) :
            p1+=1
            print(f"Player 1 wins the {x} round")
        elif np2 == 3 :
            p2+=1
            print(f"Player 2 wins the {x} round")
        else :
            print("Tie")
    elif np1 == 1 :
        if np2 == 0 :
            p2 += 1
            print(f"Player 2 wins the {x} round")
        elif np2 == 3 :
            p1 += 1
            print(f"Player 1 wins the {x} round")
        elif np2 == 2 :
            if p1 == p2 :
                print("Tie")
            elif p1 > p2 :
                p2 += 1
                print(f"Player 2 wins the {x} round")
            else :
                p1 += 1
                print(f"Player 1 wins the {x} round")
        else :
            print("Tie")
    elif np1 == 2 :
        if np2 == 0 :
            p2 += 1
            print(f"Player 2 wins the {x} round")
        elif np2 == 3 :
            p1 += 1
            print(f"Player 1 wins the {x} round")
        elif np2 == 1 :
            if p1 == p2 :
                print("Tie")
            elif p1 > p2 :
                p2 += 1
                print(f"Player 2 wins the {x} round")
            else :
                p1 += 1
                print(f"Player 1 wins the {x} round")
        else :
            print("Tie")
    elif np1 == 3 :
        if np2 == 0 :
            p1 += 1
            print(f"Player 1 wins the {x} round")
        elif np2 == 1 or np2 == 2 :
            p2 += 1
            print(f"Player 2 wins the {x} round")
        else :
            print("Tie")

    if p1 == 5 :
        print("Player 1 Won the Game")
    elif p2 == 5 :
        print("Player 2 won the Game")
