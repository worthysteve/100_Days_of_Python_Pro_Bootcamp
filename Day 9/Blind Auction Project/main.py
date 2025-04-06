from art import logo

print(logo)
# # TODO-1: Ask the user for input
# bids = {}
#
# def get_bid():
#     name = input("What is your name? ")
#     bid_amount = float(input(f"Enter your bid amount, {name}: $ "))
#     return name, bid_amount
#
# # TODO-2: Save data into dictionary {name: price}
# def add_bid(bids):
#     name, bid_amount = get_bid()
#     bids[name] = bid_amount
#     return bids
#
#
# # TODO-3: Whether if new bids need to be added
# def should_add_more_bids():
#     more_bids = input("Are there other users who want to bid? Type 'Yes' or 'No': ").lower()
#     return more_bids == 'yes'
#
# # TODO-4: Compare bids in dictionary
# def compare_bid(bids):
#     if not bids:
#         print("No bids were placed.")
#         return
#     highest_bidder = max(bids, key=bids.get)
#     highest_bid = bids[highest_bidder]
#     print(f"The highest bid is by {highest_bidder} with a bid of ${highest_bid}.")
#
# while True:
#     add_bid(bids)
#     if not should_add_more_bids():
#         break
#
# compare_bid(bids)

###################### ANGELA'S SOLUTION #########################
bids = {}

# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")

# TODO-3: Whether if new bids need to be added
continue_biding = True
while continue_biding:
    # TODO-1: Ask the user for input
    name = input("What is your name? ")
    price = float(input(f"Enter your bid amount, {name}: $ "))

    # TODO-2: Save data into dictionary {name: price}
    bids[name] = price
    should_continue = input("Are there any more bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == 'no':
        continue_biding = False
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        print("\n" * 20)


