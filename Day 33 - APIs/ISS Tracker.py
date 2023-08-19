import requests

response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# Status Code - 'Httpstatuses.com'
# 1## Hold on
# 2## Here you Go - Successful
# 3## Go away - No permission
# 4## Client Error - Doesn't exist
# 5## Server Down - Error

# # Raising Exception manually
# if response.status_code == 400:
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorized to access this data.")

# Or we can have requests do it for us
response.raise_for_status()

# Getting Data
position_data = response.json()["iss_position"]
longitude = position_data["longitude"]
latitude = position_data["latitude"]
iss_position = (longitude, latitude)

# To visualize the longitude and latitude, go to 'latlong.net'
print(iss_position)

# Some APIs require parameters

parameters = {
    "lat": 26.273714,
    "lng": 69.792169,
    "formatted": 0
}

response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
# To get hours
sunrise_time = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_time = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise_time)
print(sunset_time)