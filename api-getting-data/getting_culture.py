import requests
import json

url = "https://swapi.dev/api/people/1/"
response = requests.get(url)

data = response.json()

name = data["name"]
print("SWAPI:", name)

api_key = "apidemo"

europeana_url = "https://api.europeana.eu/record/v2/search.json"

params = {
    "wskey": api_key,
    "query": "Skywalker",
    "rows": 5
}

response = requests.get(europeana_url, params=params)

euro_data = response.json()

print("EUROPEANA:", euro_data)

with open("swapi_data.json", "w") as f:
    json.dump(data, f, indent=4)

items = euro_data.get("items", [])

with open("europeana_data.json", "w") as f:
    json.dump(items, f, indent=4)