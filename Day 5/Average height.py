students_heights = input("Input a list of student's heights : ").split(',') # input is split from the comma into multiple parts 
sum = 0
for n in students_heights:
    sum += int(n)
num_of_students = len(students_heights)
average = sum/num_of_students
# print(type(average))
average_rounded = round(average)
print(average_rounded)