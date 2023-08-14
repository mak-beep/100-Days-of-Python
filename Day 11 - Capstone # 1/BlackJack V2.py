import random

cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Get random dictionary pair in dictionary
# Using random.choice() + list() + items()
# res = k, v = random.choice(list(cards.items()))


# dealer_sum = 0

def deal_card():
    choice_ = card, value = random.choice(list(cards.items()))
    return choice_

def cards_sum(cards):
    if sum(cards) ==21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

while True:
    
    # Initializes Variables
    
    player_cards = []
    player_cards_values = []
    dealer_cards = []
    dealer_cards_values = []


    if (input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ") == 'y'):
        
        print('''
        B L A C K J A C K    
        ''')
        for i in range(2):
            player_set = deal_card()
            player_cards.append(player_set[0])
            player_cards_values.append(player_set[1])
        
        player_score = cards_sum(player_cards_values)
        print(f"Player Cards = {player_cards}, Player Total Score = {player_score}")

        for i in range(2):
            dealer_set = deal_card()
            dealer_cards.append(dealer_set[0])
            dealer_cards_values.append(dealer_set[1])
        
        print(f"First Dealer Card = ['{dealer_cards[0]}']")
        dealer_score = cards_sum(dealer_cards_values)
        

        if (player_score == 21):
            print(f"Your final hand: {player_cards}")
            print(f"Dealer's final hand: {dealer_cards}")
            print("BLACKJACK!!!")

        
        else:

            if (input("Type 'y' to get another card, type 'n' to pass: ") == 'y'):
                player_set = deal_card()
                player_cards.append(player_set[0])
                player_cards_values.append(player_set[1])
                player_score = cards_sum(player_cards_values)

        while (dealer_score<17):
            dealer_set = deal_card()
            dealer_cards.append(dealer_set[0])
            dealer_cards_values.append(dealer_set[1])
            dealer_score = cards_sum(dealer_cards_values)

        print(f"Your final hand: {player_cards}, Player Score = {player_score}")
        print(f"Dealer's final hand: {dealer_cards}, Dealer Score = {dealer_score}")

        if (player_score > 21):
            print("You Lose!")
        else:
            if (player_score > dealer_score):
                print("You Win!")

            elif (player_score == dealer_score):
                print("Draw!")
            else:
                print("You Lose!")

    else:
        quit()
                




    


