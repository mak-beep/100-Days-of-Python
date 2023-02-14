height = float(input("What is your height in m: "))
weight = float(input("What is your weight in kg: "))

bmi = weight/height**2

print("Your BMI (Complete) is "+ str(bmi))

# To get rid of decimal numbers
bmi_as_int = int(bmi)
print("Your BMI (int) is "+ str(bmi_as_int))

# to round off numbers
places = 5
bmi_rounded =round(bmi,places)
print("Your BMI (rounded) is "+ str(bmi_rounded))

# Flaot Division
bmi = weight//height**2
print("Your BMI (Float Division) is "+ str(bmi))

# F-String - Useful for joining different data types with strings - an alternative to usual
print(f"Your BMI (Float Division) is {bmi}. This is a f-string.")

# Iterative Operation
result = 4/2
result /=2
print(result)