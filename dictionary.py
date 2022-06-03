import art
#from replit import clear
#HINT: You can call clear() to clear the output in the console.

print (art.logo)

bidders = {}

end_aution = False
morebids = "no"

def calc_highest_bidder(bidders):
  max = 0
  key = ''
  bidder = bidders
  for keys in bidder:
    bid = bidder[keys]
    if bid > max:
      max = bid
      key = keys
        
  print(f"The highest bidder is {key} with bid value {max}")

while not end_aution:

  bidder_name = input("What is your name? : ")
  bid_value = int(input("How much you want to bid? : $"))
  bidders[bidder_name] = bid_value

  morebids = input("Want to continue (yes/no) : ").lower()
  if morebids == "no":
    calc_highest_bidder(bidders)
    end_aution = True
    
  else:
    #clear()
    print("continue.....")


    
    
  


  