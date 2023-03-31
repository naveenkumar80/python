from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art 
print(art.logo)
print("Welcome to Blind Auction Program")
add_user = True
def highest_bidder(bidder_record):
  highest_bid = 0
  winner = ''
  for bidders in bidder_record:
    bid_amount=bidder_record[bidders]
    if highest_bid <bid_amount:
      highest_bid=bid_amount
      winner=bidders
  print(f" {winner} has placed the highest bid of {highest_bid}")
data={}
while add_user:
  name=input("Enter the Bidder Name :")
  bid =int(input("Enter the Bid : Rs "))
  data[name]=bid
  
  want_to_continue = input("any other wants to bid write 'yes' for it or to end write 'no'")
  clear()

  if want_to_continue == 'no':
    add_user=False
    highest_bidder(bidder_record=data)

