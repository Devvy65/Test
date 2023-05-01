logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)

import random


cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


class Hand:

    def __init__(self):
        self.hand = []

    def starting_hand(self):
        starting_cards = random.choices(cards, k=2)
        self.hand.extend(starting_cards)

    def add_card(self):
        add = random.choice(cards)
        self.hand.append(add)

    def total(self):
        return sum(self.hand)

    def __str__(self):
        return f"Your cards: {self.hand}, current score: {self.total()}"


def Hit_or_Stand():
    while True:
        test = input("Type 'y' to hit, or type 'n' to stand: ")

        if test == "y":
            player_hand.add_card()
            print(player_hand)
            print(f"Dealer's first card: {dealer_hand.hand[0]}")
            if check():
                break

        elif test == "n":
            if check():
                break
            else:
                print(f"Your final hand: {player_hand.hand}, final score: {player_hand.total()}")
                print(f"Dealer's final hand: {dealer_hand.hand}, final score {dealer_hand.total()}")
                break


        else:
            print("That is not a choice please try again.")
            continue



def check():
    if player_hand.total() > 21:
        print(f"Your final hand: {player_hand.hand}, final score: {player_hand.total()}")
        print(f"Dealer's final hand: {dealer_hand.hand}, final score {dealer_hand.total()}")
        print("Bust, You lose.")
        return True

    elif dealer_hand.total() > 21:
        print(f"Your final hand: {player_hand.hand}, final score: {player_hand.total()}")
        print(f"Dealer's final hand: {dealer_hand.hand}, final score {dealer_hand.total()}")
        print("Bust, Dealer went over, you win!")
        return True

    while dealer_hand.total() < 17:
        dealer_hand.add_card()



def win():

    if player_hand.total() > 21:
        pass
    elif dealer_hand.total() > 21:
        pass
    else:
        if player_hand.total() > dealer_hand.total():
            print("You win!")

        elif player_hand.total() < dealer_hand.total():
            print("You lose!")

        elif player_hand.total() == dealer_hand.total():
            print("Draw")


player_hand = Hand()
dealer_hand = Hand()


player_hand.starting_hand()
print(player_hand)


dealer_hand.starting_hand()
print(f"Dealer's first card: {dealer_hand.hand[0]}")

Hit_or_Stand()

win()





