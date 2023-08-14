weather_c = {
    "Monday": 12,
    "Tuesday": 15,
    "Wednesday": 11,
    "Thursday": 21,
    "Friday": 32,
    "Saturday": 24,
    "Sunday": 17,
}

weather_f = {day:((temp_c*9/5)+32) for (day,temp_c) in weather_c.items()}

print(weather_f)