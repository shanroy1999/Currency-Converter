import requests
import json

artist = "Conor Maynard"
song = "Hate how much I love you"
keywords = {"time"}
url = "https://api.lyrics.ovh/v1/" + artist + '/' + song

response = requests.get(url)
json_data = json.loads(response.content)

lyrics = json_data['lyrics']

print(lyrics)

statistics = {}
for keyword in keywords:
    statistics[keyword] = lyrics.count(keyword)

print(statistics)

artist = "Maroon 5"
song = "Payphone"

url = "https://api.lyrics.ovh/v1/" + artist + '/' + song

response = requests.get(url)
json_data = json.loads(response.content)

lyrics = json_data['lyrics']

print(lyrics)

keywords = {"payphone", "time"}
statistics = {}
for keyword in keywords:
    statistics[keyword] = lyrics.count(keyword)

print(statistics)
