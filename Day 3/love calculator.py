print("Welcome to the Love Calculator!")
name1 = input("Enter your name : ")
name2 = input("Enter your crush's name : ")
name1 = name1.lower()
name2 = name2.lower()

combined_name = name1 + name2
# 'True'
t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')

true = t+r+u+e

# 'Love'
l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
e = combined_name.count('e')

love = l+o+v+e

love_score = str(true) + str(love)
print(f"Your love percentage is {love_score} %.")