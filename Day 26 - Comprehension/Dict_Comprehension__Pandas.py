# Looping through Pandas DataFrame
student_dict = {
    "student": ["Angela", "Mike", "Lily"],
    "score": [56, 87, 67]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)


# for (key,value) in student_data_frame.items():
#     print(value)


# Loop through the rows of the DataFrame
for (index,row) in student_data_frame.iterrows():
    print(row.student)