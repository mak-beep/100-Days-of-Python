students_scores = input("Input a list of student's scores : ").split(',') # input is split from the comma into multiple parts 
max_ = students_scores[0]
for n in students_scores:
    print(f"N --- {n}")
    if int(n) > int(max_):
        max_ = n
    print(f"Max ----- {max_}")
print(max_)