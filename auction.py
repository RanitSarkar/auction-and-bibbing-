import os
clear = lambda: os.system('cls')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
#HINT: You can call clear() to clear the output in the console.
print(logo)
bids={}
should_end = False

def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    # auction_list={
    # "ranit":12,"james":14 
    # }
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount> highest_bid:
            highest_bid= bid_amount
            winner=bidder
    print(f"the winner is {winner} with {highest_bid}")



while not should_end:
    name=input("type your name..?? \n")
    bid=int(input("enter your bid..?? \n $ "))
    bids[name]=bid
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    clear()
    if restart == "no":
        should_end = True
        find_highest_bidder(bids)
    elif restart == "yes":
        clear()