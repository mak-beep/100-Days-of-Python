# with open("./weather-data.csv") as data_file:
#     data = data_file.readlines()
#     for line in data:
#         print(line)

# import csv
#
# with open("./weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         temp = row[1]
#         if temp != 'temp':
#             temperature.append(temp)
#
# print(temperature)


import pandas

data = pandas.read_csv("weather-data.csv")

## Conversion
# temp_data = data["temp"].to_list()

## Average
# sum = 0
# for temp in temp_data:
#     sum += temp
# average = round(sum / len(temp_data),2)
# print('Average Temperature:', average, "Fahrenheit.")

# average = data["temp"].mean()
# print(average)

## Max Value
# max_value = data["temp"].max()
# print(max_value)

## Get data from a column
# column_data = data["condition"]
# print(column_data)
# # or we can do same thing as square bracket notation, by calling the data
# print(data.condition)


# ## Get data from a row
# row_data = data[data.day == "Monday"]
# print(row_data)

# ## To get row data, where temp is max.
# max_value = data.temp.max()

# print(data[data.temp == max_value])

# ## Convert Monday's temp from Celcius into Fahrenheit
# monday = data[data.day == 'Monday']
# monday_temp = monday.temp
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


# ## Creating a DataFrame from Scratch

data_dict = {
    "students": ["Amy", "James", "Mike"],
    "score": [76, 83, 92]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
# print(data)