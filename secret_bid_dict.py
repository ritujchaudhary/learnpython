bidders = {}

end_aution = False
morebids = "no"

def bidding():
  bidder_name = input("What is your name? : ")
  bid_value = input("How much you want to bid? : ")
  return bidder_name,bid_value

while not end_aution:
  
  bidder_name,bid_value = bidding()
  bidders[bidder_name] = bid_value

  morebids = input("Want to continue (yes/no) : ").lower
  if morebids == "yes" and end_aution == False:
    clear()
  else:
    end_aution = True
    print("the end !!")
    
  
