# num_file1 = []
# num_file2 = []

with open("Day 26 - List Comprehension/file1.txt") as file1:
    data1 = file1.readlines()
    # for data in data1:
    #     num = data.strip()
    #     num_file1.append(int(num))
    
    # print(num_file1)

with open("Day 26 - List Comprehension/file2.txt") as file2:
    data2 = file2.readlines()
    # for data in data2:
    #     num = data.strip()
    #     num_file2.append(int(num))

    # print(num_file2)


# result = [num for num in num_file1 if num in num_file2]
result = [int(num) for num in data1 if num in data2]
print(result)