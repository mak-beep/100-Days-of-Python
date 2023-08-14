def update_format(f_name, l_name):
    """Take a first and last name and format them to return
    the title case version of the string."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"


updated_string = update_format(input("What is your first name? "), input("What is your last name? "))
print(updated_string)
