
# 1. for this approach, we need to close this file manually
# file = open("my_file.txt")

# 2. Automatic Approach
# Mode = "r" for reading and "w" for writing new data completely, and "a" for append to make changes to existing data
with open("my_file.txt", mode="a") as file:
    # contents = file.read()
    # print(contents)

    file.write("Lesson Learned.")


# 1. Approach
# file.close()