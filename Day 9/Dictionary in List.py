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


def add_new_country(country, cities, visits):
    temp_country = {}
    temp_country["Country"] = country
    temp_country["cities_visited"] = cities
    temp_country["total_visits"] = visits
    travel_info.append(temp_country)


add_new_country("Russia",["Moscow", "Saint Peters",], 2)
print(travel_info)


# This type of logic is really helpfull when creating a website for recording our Travels.