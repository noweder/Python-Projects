############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

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

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run
  
#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.
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
            









    # elif user_starting_score > 21:
    #     for card in user_starting_cards:
    #         if card == 11:
    #             card = 1
    #     if user_starting_cards > 21:
    #         print("You lose")
    #     else:
            
            
    #print(f"Computer's first card: {computer_starting_cards[0]}")

        
    
    


#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_starting_cards = []
#computer_starting_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_starting_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_starting_cards and computer_starting_cards. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_starting_cards is over 21, then the user loses. If the computer_starting_cards is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.