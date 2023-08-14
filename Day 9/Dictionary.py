# Major difference between Dictionary and List:
#  In lists, values are accessed by the index
#  In Dictionaries, values are accessed by their Keys






contact = {'FirstName' : 'Moaaz', 'LastName' : 'Ahmad'}

# Retrieving an item from the dictionary
print(contact['FirstName'])

# Adding new entries
contact['Age'] = 22

print(contact)

#  Empty Dictionary

empty_dict = {}

# # Wiping an existing dictionary

# contact = {}
# print(contact)


# Editing the dict.
contact['Age'] = 20
#  if key doesn't eist, it will create a new one of the same name.
print(contact)


# For looping through the dict.
for key in contact:
    print(key)
    print(contact[key])

