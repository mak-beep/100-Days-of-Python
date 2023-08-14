def welcome():
    print("Hi!")
    print("Welcome to our neighbourhood.")

welcome()

# Arguments
def special_welcome(name):
    print("Hi "+name)
    print("Welcome to our neighbourhood.")

neighbour = 'Angela'
special_welcome(neighbour)

# Advanced Arguments
# To give a default value if not specified
def welcome_neighbour(name="Mak"):
    print("Hi "+name)
    print("Welcome to our neighbourhood.")

welcome_neighbour()
welcome_neighbour("John")

# Unlimited Arguments - Call by Position
def add(*nums):
    # num is a tuple
    # individual members can be accessed
    print(nums[0])
    sum = 0
    for n in nums:
        sum += n

    return sum

print(add(1,2,3,4,5))

# Unlimited Arguments - Call by Keyword
def calculate(**nums):
    # nums is a ditionary - Members can be accessed by keyword

    # for key,value in nums.items():
    #     print(key)
    #     print(value)

    print(nums["add"])
    # if add is not provided, it will give error. To avoid that use .get() method.
    print(nums.get("add"))

calculate(add=3,multiply=7)