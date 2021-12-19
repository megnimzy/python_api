import requests

parameters = {
    "lat": 40.71,
    "lon": -74
}
print("Hello Linux and Github!")

response = requests.get("https://api.open-notify.org/astros.json")

jprint(response.json())