letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
arr_size = len(letters)-1

# Part 1 - Encode
def encryp(x, y):
    print(x)
    encrypted_word = ""
    for i in range(len(x)):
        if x[i] == ' ':
            encrypted_word += ' '
        j = 0
        for letter in letters:
            if letter == x[i]:
                shift = j+y
                if shift > arr_size:
                    shift = shift - arr_size
                encrypted_word += letters[shift]
            j += 1
    
    return encrypted_word

# Part 2 - Decode
def decrypt(x, y):
    print(x)
    decrypted_word = ""
    for i in range(len(x)):
        if x[i] == ' ':
            decrypted_word += ' '
        j = 0
        for letter in letters:
            if letter == x[i]:
                shift = j-y
                if shift < 0:
                    shift = shift + arr_size
                decrypted_word += letters[shift]
            j += 1
    
    return decrypted_word


# Part 3 - Combined Approach - V1
def cesar(x,y,direction):
    new_Word = ""
    # letters.index(letter)
    for i in range(len(x)):
        if x[i] == ' ':
            new_Word += ' '
        j = 0
        for letter in letters:
            if letter == x[i]:
                if direction == -1:
                    shift = j-y
                    if shift < 0:
                        shift = shift + arr_size
                elif direction == 1:
                    shift = j+y
                    if shift > arr_size:
                        shift = shift - arr_size
                new_Word += letters[shift]
            j += 1
    return new_Word
# Part 3 - Combined Approach - V2
def cesar_(x,y,direction):
    new_Word = ""
    if direction == "decode":
        y *= -1
    for letter in x:
        if letter == ' ':
            new_Word += letter
        elif letter in letters:
            position = letters.index(letter)
            new_position = position + y
            if new_position < 0:
                new_position = new_position + arr_size
            if new_position > arr_size:
                new_position = new_position - arr_size
            new_Word += letters[new_position]
        else:
            new_Word += letter

    print(f"Your message was '{x}'.\nYour {direction}d word is '{new_Word}'.")

# Part 4 - TODO 1 - 3

# while True:
    # user_input = input("Enter the message : ").lower()
    # option = input("What do you want to do?\n 1.encode 2.decode\n").lower()
    # shift_amount = int(input("Enter Shift number : "))
    # if shift_amount>len(letters):
    #     shift_amount %= len(letters)

    # cesar_(user_input,shift_amount,option)
    # restart_option = input("Do you want to restart the program?\n1.Yes 2.No\n").lower()
    # if restart_option == 'no':
    #     break


# phrase = user_input.replace(" "," ")
# if option == 'encode':
#     # new_word = encryp(phrase,shift_code)
#     new_Word = cesar(phrase,shift_code,1)
#     print(f"Your message was '{phrase}'.\nYour Encrypted Code is '{new_Word}'.")
# elif option == 'decode':
#     # new_word = decrypt(phrase,shift_code)
#     new_Word = cesar(phrase,shift_code,-1)
#     print(f"Your message was '{phrase}'.\nYour Decrypted Code is '{new_Word}'.")


# TODO 4

def cesar_cipher():
    user_input = input("Enter the message : ").lower()
    option = input("What do you want to do?\n 1.encode 2.decode\n").lower()
    shift_amount = int(input("Enter Shift number : "))
    if shift_amount>len(letters):
        shift_amount %= len(letters)

    cesar_(user_input,shift_amount,option)
    restart_option = input("Do you want to restart the program?\n1.Yes 2.No\n").lower()
    if restart_option == 'yes':
        cesar_cipher()

cesar_cipher()