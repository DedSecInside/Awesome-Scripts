import random 
coin = ["Heads","Tails"]
toss = random.choice(coin)
selection = input("Heads or Tails: ")
if selection == toss:
    print("You won! the coin landed on" + toss)
else:
    print("You lost! the coin landed on" + toss)
