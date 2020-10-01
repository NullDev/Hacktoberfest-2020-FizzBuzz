from random import shuffle #Basic library
SUITE = 'H D S C'.split() # H:Hearts----D:Diamonds------S:Spades-------C:Clubs
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split() #card names

#Deck Class
class Deck:
    def __init__ (self):
        self.theDeck = [(s,r) for s in SUITE for r in RANKS ]
        print("Created new deck (ordered)!")

    def split_in_half(self):
        return (self.theDeck[:26],self.theDeck[26:])

    def shuffle(self):
        shuffle(self.theDeck)
        print("Shuffling!")

#Specific Hand class
class Hand:
    def __init__(self,cards):
        self.cards = cards

    def add_card(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


    def __str__(self):
        return "Has {} cards".format(len(self.cards))

#For each player
class Player:
    def __init__(self, hand, name):
        self.hand = hand
        self.name = name

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has played: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) <3:
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) != 0


# GAME#

print("Welcome to War!")



d = Deck()
d.shuffle()
cut1,cut2 = d.split_in_half()


cdeckWeight=0

comp = Player(Hand(cut1),"Computer Player")
name = input("Enter Your Name: ")
user = Player(Hand(cut2),name)

for each in cut2:
    if '9' in each:
        cdeckWeight +=1
for each in cut2:
    if '10' in each:
        cdeckWeight +=2
for each in cut2:
    if 'J' in each:
        cdeckWeight +=3
for each in cut2:
    if 'Q' in each:
        cdeckWeight +=4
for each in cut2:
    if 'K' in each:
        cdeckWeight +=5
for each in cut2:
    if 'A' in each:
        cdeckWeight +=6
for each in cut2:
    if '7' in each:
        cdeckWeight +=(-1)
for each in cut2:
    if '6' in each:
        cdeckWeight +=(-2)
for each in cut2:
    if '5' in each:
        cdeckWeight +=(-3)
for each in cut2:
    if '4' in each:
        cdeckWeight +=(-4)
for each in cut2:
    if '3' in each:
        cdeckWeight +=(-5)
for each in cut2:
    if '2' in each:
        cdeckWeight +=(-2)
vicProb = 7.67*(10**(-3))*cdeckWeight+(0.504)

#initializing the game
total_rounds = 0
numberOfWar= 0
doubleWarCount =0
exceptCount =0


while user.still_has_cards() and comp.still_has_cards():
    total_rounds +=1
    print("New round!")
    print("Here is the Score!")
    print(user.name+" has "+str(len(user.hand.cards))+" cards left")
    print(comp.name+" has "+str(len(comp.hand.cards))+" cards left")
    print("Now play a card!")
    print("\n")

    cards_on_table = []
    computer_card = comp.play_card()
    player_card = user.play_card()

    cards_on_table.append(computer_card)
    cards_on_table.append(player_card)

    if computer_card[1] == player_card[1]:
        numberOfWar +=1
        print(computer_card[1])
        print("WAR HAS BEGUN!")
        cards_on_table.extend(user.remove_war_cards())
        cards_on_table.extend(comp.remove_war_cards())

        try:
            computer_card = comp.play_card()
            player_card = user.play_card()

            cards_on_table.append(computer_card)
            cards_on_table.append(player_card)

            if RANKS.index(computer_card[1]) < RANKS.index(player_card[1]):
                user.hand.add_card(cards_on_table)
            elif RANKS.index(computer_card[1]) == RANKS.index(player_card[1]):
                doubleWarCount +=1
                print("NOW WE HAVE DOUBLE WAR!")
                cards_on_table.extend(user.remove_war_cards())
                cards_on_table.extend(comp.remove_war_cards())
                try:
                    computer_card = comp.play_card()
                    player_card = user.play_card()

                    cards_on_table.append(computer_card)
                    cards_on_table.append(player_card)
                    if RANKS.index(computer_card[1]) < RANKS.index(player_card[1]):
                        user.hand.add_card(cards_on_table)

                    else:
                        comp.hand.add_card(cards_on_table)

                except:
                    exceptCount =+1
                    print("Not Enough Cards for Double War")
                    break
            else:
                comp.hand.add_card(cards_on_table)

        except:
            exceptCount +=1
            print("Not enough cards left in deck for War, Game over")
            break;

    else:
        if RANKS.index(computer_card[1]) < RANKS.index(player_card[1]):
            user.hand.add_card(cards_on_table)
        else:
            comp.hand.add_card(cards_on_table)
if exceptCount>=1: #remaining card counter
    if len(user.hand.cards)>len(comp.hand.cards):
        print(user.name+" has Won!")
    else:
        print("Computer Player has Won!")
else:
    if len(user.hand.cards)==0:
        print("Game Over! Computer Player has Won!")
    else:
        print("Game Over! "+user.name+" has Won!")

#LAST MESSAGE
print("Good Game, there were "+str(total_rounds)+" rounds!")
print("War happened "+str(numberOfWar)+" times.")
print("Double War happened "+str(doubleWarCount)+" times.")
print("War games that didnt finish: "+str(exceptCount))

print(user.name+" had a "+str(vicProb)+" probability of winning of due to deck weight")
