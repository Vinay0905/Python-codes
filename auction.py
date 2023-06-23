from replit import clear
#HINT: You can call clear() to clear the output in the console.from art 
from art import logo
print(logo)


bids=[]
bidding_finished=False
def find_highest_bidder(bidding_record):
  highest_bid=0
  for bidder in bidding_record:
    bid_amount=bidding_record[bidder]
    if bid_amount> highest_bid:
      highest_bid=bid_amount
      winner=bidder
  print(f"The winner is {winner}.")
  
while not bidding_finished:
  user_name=input("What is your name?:")
  Bid_price=input("What's your bid price?: $")
  bids[user_name]=Bid_price
  
  should_continue= input("Are there any more bidders?type 'yes' or 'no'.")
  if should_continue=='no':
    bidding_finished=True
  elif should_continue=='yes':
    clear()


  