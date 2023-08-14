import pandas

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

color = data["Primary Fur Color"]

gray_squirrel_count = len(color[color=="Gray"])
cinnamon_squirrel_count = len(color[color=="Cinnamon"])
black_squirrel_count = len(color[color=="Black"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("Squirrel_count.csv")