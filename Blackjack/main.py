############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import os, platform
import random

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def is_blackjack(cards):
    if sum(cards) == 21:
        return True
def deal_card(cards, num):
    return random.sample(cards, num)

def score(cards):
    return sum(cards)


current_score = 0
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
is_continue = True
while is_continue == True:

    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        clear()
        print(logo)
        user_starting_cards = deal_card(cards, 2)
        computer_starting_cards = random.sample(cards, 2)
        print(f"    Your cards: {user_starting_cards}, current score: {score(user_starting_cards)}")
        print(f"    Computer's first card:  {computer_starting_cards[0]}")    

        if is_blackjack(computer_starting_cards) == True: 
            print("You Lose")
        elif is_blackjack(user_starting_cards) == True:
            print("You Win with Blackjack!")

        else:
            another_card = True
            while another_card == True:

                if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                    user_new_card = random.choice(cards)
                    user_starting_cards.append(user_new_card)
                    if score(user_starting_cards) > 21:
                        for card in user_starting_cards:
                            if card == 11:
                                card = 1

                        if score(user_starting_cards) > 21:
                            print(f"    Your cards: {user_starting_cards}, current score: {score(user_starting_cards)}")
                            print(f"    Computer's first card: {computer_starting_cards[0]}")
                            #print("You went over. You lose 😭")
                            another_card = False

                    elif score(user_starting_cards) < 21:
                        print(f"    Your cards: {user_starting_cards}, current score: {score(user_starting_cards)}")
                        print(f"    Computer's first card: {computer_starting_cards[0]}")
                else:
                    another_card = False

            while score(computer_starting_cards) < 17:
                computer_starting_cards.append(random.choice(cards))
            
            print(f"    Your final hand: {user_starting_cards}, final score: {score(user_starting_cards)}")
            print(f"    Computer's final hand: {computer_starting_cards}, final score: {score(computer_starting_cards)}")
            
            if score(computer_starting_cards) == score(user_starting_cards):
                print("It's a draw!")
            elif score(computer_starting_cards) == 21:
                print("Blackjack for computer. You lose!")
            elif score(user_starting_cards) == 21:
                print("You win with Blackjack!")
            elif score(user_starting_cards) > 21:
                print("You went over. You lose 😭")
            elif score(user_starting_cards) > score(computer_starting_cards) or score(computer_starting_cards) > 21:
                print("You still win")
            else:
                print("You lost")

    else:
        is_continue = False
            









    
        
    
    


