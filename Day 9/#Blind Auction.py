import os

bid_info = {}
print("Welcome to Secret Bidding Auction.")
def auction_bid():
    bidder= {}
    name = input("What is your Name?: ")
    bid = int(input("What's your bid?: $"))
    bid_info[name] = bid

finished = False
def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"{winner} has made the highest bid of ${highest_bid}.")
while (~finished):
    auction_bid()
    should_continue = input("Any more Bidders : Yes or No --- ").lower()
    if should_continue == "no":
        finished = True
        highest_bidder(bid_info)
    elif should_continue == "yes":
        os.system('cls')


    
# website for debugging ------- pythontutor.com

