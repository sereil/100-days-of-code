from ast import While
import os
import art



print(art.logo)

bidders = {}
end_auction = False

def find_highest_bidder(bidding_record):
    highest_bidder = ""
    highest_bid = bidding_record
    for bidder in bidders:
        current_bid = bidders[bidder]
        if current_bid > highest_bid:
            highest_bid = current_bid
            highest_bidder = bidder
    print(f"The highest bidder was {highest_bidder} with a bid of ${highest_bid}!")

while not end_auction:    
    name = input("Enter your name: ").lower()
    bid = int(input("Enter your bid: $"))
    
    bidders[name] = bid

    other_bids = input("Are there any other bidders? Type yes or no: ").lower()

    if other_bids == "no":
        end_auction = True
    elif other_bids == "yes":
        os.system('CLS')
    
if end_auction == True:
    highest_bid = 0
    find_highest_bidder(highest_bid)
