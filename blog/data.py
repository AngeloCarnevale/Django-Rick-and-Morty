import requests


posts = requests.get("https://rickandmortyapi.com/api/character").json()["results"]

print(posts[0]["image"])