import random

cards = []
suits = ["hearts", "diamonds", "clubs", "spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
user_cards = []

for suit in suits:
    for rank in ranks:
        cards.append([rank, suit])

def shuffle():
    random.shuffle(cards)

def deal(amount):
    for i in range(amount):
        user_cards.append(cards.pop())
    return user_cards

def start():
    shuffle()
    user_input = int(input("How many cards do you want to deal? "))
    print(deal(user_input))

start()