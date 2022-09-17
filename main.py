# welcome to the auction program
# name, bid, asking a human 'are there any bidders ? "yes" or "no"

from replit import clear

print("welcome to the auction program.")



bids = {}
bidding_finished = False

def find_higgest_bidder(bidding_record):
    highest_bit = 0
    winner =""
    # bidding_recordkaan : 12dolar james:45 dolar gibi olacak
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bit:
            highest_bit = bid_amount
            winner = bidder
    print(f"winner is {winner}, with price :{highest_bit} ")

while not bidding_finished:
    name = input("enter a name: ")
    price = int(input("enter a price: $"))
    bids[name] = price
    should_continue = input("are there any other biders ?  'yes' or 'no' ")
    
    
    if should_continue == "no":
        bidding_finished = True
        find_higgest_bidder(bids)
        print("auction finished. ")
    elif should_continue =="yes":
        clear()