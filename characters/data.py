import requests


posts = requests.get(f"https://rickandmortyapi.com/api/character").json()["results"] 




    
