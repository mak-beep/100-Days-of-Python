student_scores = {"Harry": 81,
                  "Ron": 78,
                  "Hermione": 99,
                  "Draco": 74,
                  "Neville": 62,}

student_grades = {}

for key in student_scores:
    score = student_scores[key]
    if score >= 91:
        grade = "Outstanding"
    elif score >=81:
        grade = "Exceeds Expectations"
    elif score >= 71:
        grade = "Acceptable"
    elif score <= 70:
        grade = "Fail"

    student_grades[key] = grade
    
print(student_scores)
print(student_grades)