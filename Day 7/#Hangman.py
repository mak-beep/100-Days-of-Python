import random
import Hangman_word_list as wl
import Hangman_art as art

lives = 6
isComplete = False
correct_Letters = 0

chosen_word = random.choice(wl.word_list)
guess_word = []
for letter in chosen_word:
    guess_word += "_"

tries = []

# word_set = set(chosen_word)
# word_len = len(word_set)


# while not isComplete:
#     user_input = input("Choose a character : ")
    
#     for letter in chosen_word:
#     if user_input in chosen_word:
#         print("You have chosen the correct letter.")
#         correct_Letters += 1
#         print(correct_Letters)
#     else:
#         print(f"Wrong!!! A Life Lost. Remaining lives = {lives}")
#         lives -= 1
#     if lives == 0:
#         print("You have run out of lives.")
#         isComplete = True
#     elif correct_Letters >= word_len:
#         print("You have guessed it correctly.")
#         isComplete = True


in_word = False
print(art.logo)
while not isComplete:
    user_input = input("Enter a guess : ").lower()
    i = 0
    
    if user_input not in tries:
        tries += user_input
        in_word = False
        for letter in chosen_word:
                
            if letter == user_input:
                guess_word[i] = user_input
                in_word = True
            i+=1

        if in_word == False:
            lives -= 1
            print(f"You guessed {user_input}, thats not in the word. You lose a life.")
            print(f"Remaining Lives = {lives}")
            if lives == 0:
                print("You Lose!!!")
                isComplete = True
        if "_" not in guess_word:
            print("You win!!!")
            isComplete = True
    else:
        print(f"You have already guessed '{user_input}'.")
    print(f"{' '.join(guess_word)}")
    print(art.stages[lives])