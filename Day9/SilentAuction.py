import os
from SilentAuctionArt import logo

print(logo)
print("Welcome to the Silent Auction.")
next_person = True
bidders = {}
amount_list = []
while next_person:
    name = input("Please enter your name: ")
    amount = int(input("Please enter your bidding amount: $"))
    amount_list.append(amount)
    bidders[name] = amount
    next = input("Are there more people to bid?\nYes or No\n").lower()
    os.system('cls')
    if next == 'no':
        next_person = False
        for k, v in bidders.items():
            if v == max(amount_list):
                print(f"The winner of the auction is {k} with the bid amount of ${v}.")
