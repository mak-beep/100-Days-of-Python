
def greet(name, location):
    print(f"Hi {name},")
    print(f"What is it like in {location}?")

# Positional Arguments
# Order of arguments is important, it wil always consider the first argument as an input for 'name'
greet("Moaaz", "Islamabad")
greet("Islamabad", "Moaaz")

# Keyword Arguments
# Order of arguments does not matter, it will focus on the value assigned to variables.
greet(location="Islamabad",name="Moaaz")