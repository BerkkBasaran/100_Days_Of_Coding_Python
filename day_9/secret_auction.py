print("Welcome to the secret auction program.")

bid_dictionary = {}

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner} with a bid of ${highest_bid}.")

multibidders = True

while multibidders:
    
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bid_dictionary[name] = price
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if other_bidder == "no":
        multibidders = False
        find_highest_bidder(bid_dictionary)
    elif multibidders == "yes":
        print("\n" * 40)




        













