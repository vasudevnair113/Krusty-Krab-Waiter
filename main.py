print("Bot: Hello human being!")
print("     How are you today?")
feeling = input("You: ")

foundGood = False
for i in range(0, len(feeling) - 3):
  if feeling[i:i+4].lower() == "good":
    foundGood = True
if foundGood:
  print("Bot: Nice to hear that!")
else:
  print("Bot: I'm sorry to hear that.")

'''
feelingsplit = feeling.split()
for i in feelingsplit():
  if i.lower() == "good" or i.lower() == "good!" or i.lower:
    print("Bot: Nice to hear that!")
  elif i.lower() == "bad":
    print("Bot: I'm sorry to hear that.")
'''
'''
if feeling.lower() == "good":
  print("Bot: Nice to hear that!")
elif feeling.lower() == "bad":
  print("Bot: I'm sorry to hear that.")
'''
print("Bot: Do you have an allergy to Kelp, Coral, or Krab meat?") 
allergyconfirm = input("You: ")
if allergyconfirm.lower() != "no":
  print("Bot: What are you allergic to?")
  allergy = input("You: ")


ordersize = {}
totalcost = 0

def noallergy():
  print("Bot: What would you like to order? We have Kelp shakes, Coral bits, and our world famous Krabby Patties.")
def kelpallergy():
  print("Bot: What would you like to order? We have Coral bits and our world famous Krabby Patties.")
def coralallergy():
  print("Bot: What would you like to order? We have Kelp shakes and our world famous Krabby Patties.")
def kraballergy():
  print("Bot: What would you like to order? We have Kelp shakes and Coral bits.")


while True:
  if allergyconfirm.lower() == "no":
    noallergy()
  elif allergy.lower() == "kelp":
    kelpallergy()
  elif allergy.lower() == "coral":
    coralallergy()
  elif allergy.lower() == "krab" or allergy.lower() == "krab meat":
    kraballergy()
  order = input("You: ")

  print("Bot: What size? We have small, medium, and large. For Krabby Patties, we have single, double, and triple.")
  size = input("You: ")
  ordersize[order] = size
  if order.lower() == "kelp shake" and size.lower() == "small":
    totalcost += 1.00
  elif order.lower() == "kelp shake" and size.lower() == "medium":
    totalcost += 1.25
  elif order.lower() == "kelp shake" and size.lower() == "large":
    totalcost += 1.50
  elif order.lower() == "coral bits" and size.lower() == "small":
    totalcost += 1.00
  elif order.lower() == "coral bits" and size.lower() == "medium":
    totalcost += 1.25
  elif order.lower() == "coral bits" and size.lower() == "large":
    totalcost += 1.50
  elif order.lower() == "krabby patty" and size.lower() == "single":
    totalcost += 1.25
  elif order.lower() == "krabby patty" and size.lower() == "double":
    totalcost += 2.00
  elif order.lower() == "krabby patty" and size.lower() == "triple":
    totalcost += 3.00

  print("Bot: Would you like anything else?")
  wouldlike = input("You: ")
  if wouldlike.lower() == "no":
    break

print("Bot: Okay, you ordered:")
for i in ordersize:
  print("Bot:", i, "-", ordersize[i])
print("Bot: Your total cost is: $",totalcost)