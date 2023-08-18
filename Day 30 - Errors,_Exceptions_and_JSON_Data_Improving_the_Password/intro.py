# Components

# try:
    # Something that can cause an exception (unexpected behavior)

# except: (We can have multiple exceptions)
    # What happens if there is an exception

# else:
    # Do this if there is no exception, and try is successful

# finally:
    # Do this, no matter what


try:
    file = open(file = "./data.txt")

    a_dictionary = {"key": "value"}
    print(a_dictionary["another_key"])

# Only one exception will be considered in a process at a time
except FileNotFoundError:
    file = open(file = "./data.txt", mode='w')

except KeyError:
    print("That key doesn't exist.")
else:
    print("Hello")

finally:
    print("Process End.")
    # We can also raise an error by ourselves
    raise KeyError("This is an error raised by the user.")

