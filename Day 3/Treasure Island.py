print("Welcome to the Treasure Island.\n")
print("Your mission is to find the treasure.")

choice1 = input("You are at a crossroad. Where do you want to go? Type 'Left' or 'Right'\n")
if choice1 == 'Right':
    print("Game Over.")
elif choice1 == 'Left':
    choice2 = input("You came to a lake. There is an island in the middle of the lake. Type 'Wait' to wait for a boat. Type 'Swim' to swim across.\n")
    if choice2 == 'Swim':
        print("You got attacked by an angry trout. Game Over.")
    elif choice2 == 'Wait':
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which door do you choose?\n")
        if choice3 == 'Red':
            print("It's a room full of fire. Game Over.")
        elif choice3 == 'Blue':
            print("You enter a room of beasts. Game Over.")
        elif choice3 == 'Yellow':
            print("You Won!")

