import requests


posts = []
for i in range(1, 200):
    post = requests.get(f"https://rickandmortyapi.com/api/character/{i}").json()
    posts.append(post)






    
