import random

cards = []
suits = ["hearts", "diamonds", "clubs", "spades"]
ranks = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

for suit in suits:
    for rank in ranks:
        cards.append([rank, suit])

def shuffle():
    random.shuffle(cards)

def deal(amount):
    for i in range(amount):
        return cards.pop()

def start():
    shuffle()
    user_input = int(input("How many cards do you want to deal? "))
    for i in range(user_input):
        print(deal(1))

start()