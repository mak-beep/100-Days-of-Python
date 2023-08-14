Capitals = {
    "France": "Paris",
    "Pakistan": "Islamabad",
}

travel_logs = {
    "France": ["Paris", "Dijon", "Lille"],
    "Pakistan": ["Islamabad", "Karachi", "Lahore"],
}

travel_info = {
    "France": {"cities_visited": ["Paris", "Dijon", "Lille"], "total_visits": 12},
    "Pakistan": {"cities_visited": ["Islamabad", "Karachi", "Lahore"], "total_visits": 8},
}

print(Capitals)
print(travel_logs)
print(travel_info)

#  Dictionaries in a List
travel_info = [
    {
        "Country": "France",
        "cities_visited": ["Paris", "Dijon", "Lille"],
        "total_visits": 12
    },
    {
        "Country": "Pakistan",
        "cities_visited": ["Islamabad", "Karachi", "Lahore"],
        "total_visits": 8
    },
]

print(travel_info[0]['Country'])