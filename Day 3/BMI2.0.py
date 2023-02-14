height = float(input("What is your height in m: "))
weight = float(input("What is your weight in kg: "))

bmi = weight/height**2
places = 2
bmi =round(bmi,places)
print("Your BMI (Complete) is "+ str(bmi))

if (bmi<18.5):
    print("You are underweight.")
elif (bmi<25):
    print("You have a normal weight. ")
elif (bmi<30):
    print("You are overweight.")
elif (bmi<35):
    print("You are obese.")
elif (bmi>=35):
    print("You are clinically obese.")

