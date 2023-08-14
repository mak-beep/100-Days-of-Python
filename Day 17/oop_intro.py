class User:
    def __init__(self, name, id, age, location, followers):
        self.name = name
        self.id = id
        self.age = age
        self.location = location
        self.followers = followers
        print("New User is created.")

    def moved_to(self, location):
        self.location = location


user_1 = User("Moaaz",191889,23, "Pakistan", "500k")

print(user_1.location)
user_1.moved_to("Faisalabad")
print(user_1.location)
