import random

cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': [1,11]}

# Get random dictionary pair in dictionary
# Using random.choice() + list() + items()
# res = k, v = random.choice(list(cards.items()))

player_cards = []
player_sum = 0
dealer_cards = []
dealer_sum = 0

def get_player_card(player_sum):
    choice_ = card, value = random.choice(list(cards.items()))
    # player_cards[card] = value
    player_cards.append(card)
    if (card == 'A'):
        player_sum = player_sum + value[11]
        return player_sum
    player_sum = player_sum + value
    return player_sum

def get_dealer_card(dealer_sum):
    choice_ = card, value = random.choice(list(cards.items()))
    # player_cards[card] = value
    dealer_cards.append(card)   
    if (card == 'A'):
        value = 11
    dealer_sum += value
    return dealer_sum 

while True:
    if (input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ") == 'y'):
        
        print('''
        B L A C K J A C K    
        ''')
        for i in range(2):
            player_sum = get_player_card(player_sum)
        

        print(f"Player Cards = {player_cards}")
        for i in range(2):
            dealer_sum = get_dealer_card(dealer_sum )

        
        print(f"First Dealer Card = ['{dealer_cards[0]}']")

        if (player_sum == 21):
            print(f"Your final hand: {player_cards}")
            print(f"Dealer's final hand: {dealer_cards}")
            print("BLACKJACK!!!")

        elif (player_sum > 21) or (dealer_sum >= 21):
            if 'A' in player_cards:
                print("Counting Ace as '1' instead of '11'")
                player_sum -= 10

            else:
                print(f"Your final hand: {player_cards}")
                print(f"Dealer's final hand: {dealer_cards}")
                print("You Lose!")
        
        else:

            if (input("Type 'y' to get another card, type 'n' to pass: ") == 'y'):
                player_sum = get_player_card(player_sum)
                # dealer_sum = get_dealer_card(dealer_sum)

            print(f"Your final hand: {player_cards}")
            print(f"Dealer's final hand: {dealer_cards}")

            if (player_sum > 21):
                print("You Lose!")
            else:
                player_difference = 21 - player_sum
                dealer_difference = 21 - dealer_sum
                if (player_difference < dealer_difference):
                    print("You Win!")

                elif (player_difference == dealer_difference):
                    print("Draw!")
                else:
                    print("You Lose!")

    else:
        quit()
                




    


