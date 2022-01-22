import os, platform
from art import logo
print(logo)

bidding_finished = False
bids = {}

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def find_highest_bidder(bidding_record):
    highest_bid_value = 0
    winner = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bid_value:
            highest_bid_value = bidding_record[bidder]
            winner = bidder
    print(f"The winner is {winner} with bid of ${bids[winner]}")
    
while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    other_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if other_bidders == "yes":
        clear()
    elif other_bidders == "no":
        bidding_finished = True

find_highest_bidder(bids)