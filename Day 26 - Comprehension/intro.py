# ## List Comprehension

num = [1,2,3,4]
new_number = [n+1 for n in num]
print(new_number)
doubled_list = [n+n for n in range(1,5)]
print(doubled_list)


names = ["Joseph", "John", "Mak","Delphine", "Smith"]
modified_names = [name.upper() for name in names if len(name)<5]
print(modified_names)


# ## Dictionary Comprehension
import random

students_scores = {student:random.randint(1,100) for student in names}

print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score > 50}

print(passed_students)