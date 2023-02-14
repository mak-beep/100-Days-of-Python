import random

names_string = input("Give me the names separated by a comma.\n")

names = names_string.split(", ")
length = len(names)
player_no = random.randint(0, length)
loser = names[player_no]
print(f"{loser} will pay for the meal today!!")