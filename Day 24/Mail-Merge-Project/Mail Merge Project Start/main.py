#TODO: Create a letter using starting_letter.txt 

PLACEHOLDER = "[name]"
#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt", mode="r") as guest_list:
    guests = guest_list.readlines()

#Replace the [name] placeholder with the actual name.
with open("./Input/Letters/starting_letter.txt", mode="r") as invitation:
    invitation_letter = invitation.read()
    for guest in guests:
        name = guest.strip()
        custom_invitation = invitation_letter.replace(PLACEHOLDER, name)
#Save the letters in the folder "ReadyToSend".
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter:
            letter.write(custom_invitation)


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp