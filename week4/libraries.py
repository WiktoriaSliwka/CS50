import random
# coin = random.choice(["heads", "tails"])
# print(coin)

# from random import choice #loads it into the local namespace
# coin = choice(["heads", "tails"])
# print(coin)

#randint = random integer
# number = random.randint(1,10)
# print(number)
#random.shuffle(x)

cards = ["Jack", "Queen", "King"]
random.shuffle(cards)
for card in cards:
    print(card)


