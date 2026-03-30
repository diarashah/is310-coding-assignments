import requests

api_key = ""

url = "https://the-one-api.dev/v2/character"

headers = {
    "Authorization": "Bearer " + api_key
}

response = requests.get(url, headers=headers)

print(response.status_code)


data = response.json()

print(data["total"])

for character in data["docs"]:
    print(character["name"])

for character in data["docs"]:
    if character["name"] == "Galadriel":
        print(character)


url = "https://the-one-api.dev/v2/character?name=Galadriel"

response = requests.get(url, headers=headers)

print(response.json())