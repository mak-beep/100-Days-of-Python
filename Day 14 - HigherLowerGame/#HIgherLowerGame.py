import os
from art import *
from game_data import data
import random
from time import sleep
score = 0
prev_Choice  = {}
choice1 = random.choice(data)
choice2 = random.choice(data)

def format_data(account):
    """Formats the data and displays it"""
    return f"{account['name']}, a {account['description']} from {account['country']}."

while True:
    print(logo)
    while (choice2 == choice1 or prev_Choice== choice2):
        choice2 = random.choice(data)
    
    print(f"Compare A: {format_data(choice1)}")
    print(vs)
    print(f"Compare B: {format_data(choice2)}")
    guess=input("Who has more followers? Type 'A', or type 'B': ").lower()
    if (guess == 'a'):
        if (choice1['follower_count'] > choice2['follower_count']):
            score += 5
            winner = f"You are Right. Current Score is {score}"
            print(winner)
            
        else:
            print(f"You got it wrong. Your Final Score is {score}.")
            quit()
    elif (guess == 'b'):
        if (choice2['follower_count'] > choice1['follower_count']):
            score += 5
            winner = f"You are Right. Current Score is {score}"
            print(winner)
            choice1 = choice2
        else:
            print(f"You got it wrong. Your Final Score is {score}.")
            quit()

    prev_Choice = choice2
    sleep(2)
    os.system('cls')