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
        choice = input("Type 'y' to hit, or type 'n' to stand: ")

        if choice == "y":
            player.add_card()
            aces()
            print(player)
            print(f"Dealer's first card: [{dealer.hand[0]}, *]")
            if bust():
                break

        elif choice == "n":
            aces()
            check()
            if bust():
                break
            else:
                print(f"Your final hand: {player.hand}, final score: {player.total()}")
                print(f"Dealer final hand: {dealer.hand}, final score: {dealer.total()}")
                win()
            break

        else:
            print("That was not a valid choice, try again.")
            continue


def check():
    while dealer.total() < 17:
        dealer.add_card()


def bust():
    if player.total() > 21:
        print(f"Your final hand: {player.hand}, final score: {player.total()}")
        print(f"Dealer final hand: {dealer.hand}, final score: {dealer.total()}")
        print("Bust you lose.")
        return True

    elif dealer.total() > 21:
        print(f"Your final hand: {player.hand}, final score: {player.total()}")
        print(f"Dealer final hand: {dealer.hand}, final score: {dealer.total()}")
        print("Dealer bust you win!")
        return True


def aces():
    if 11 in player.hand and player.total() > 21:
        for i in range(len(player.hand)):
            if player.hand[i] == 11:
                player.hand[i] = 1

    if 11 in dealer.hand and dealer.total() > 21:
        for i in range(len(dealer.hand)):
            if dealer.hand[i] == 11:
                dealer.hand[i] = 1


def win():

    if player.total() > dealer.total():
        print("You win!")

    elif player.total() < dealer.total():
        print("You lose.")

    elif player.total() == dealer.total():
        print("Draw")


playing = True

while True:

    player = Hand()
    dealer = Hand()

    def game():
        print(logo)

        player.hand = []
        dealer.hand = []

        player.starting_hand()
        print(player)
        dealer.starting_hand()
        print(f"Dealer's first card: [{dealer.hand[0]}, *]")

        Hit_or_Stand()
    game()

    break


while playing:

    again = input("Would you like to play again? type 'y' or 'n' ")

    if again == "y":
        game()
    elif again == "n":
        print("Thanks for playing please play again soon.")
        playing = False
    else:
        print("That was not an option, please pick again.")
        continue
