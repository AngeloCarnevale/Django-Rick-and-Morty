import requests


posts = []
for i in range(1, 10):
    post = requests.get(f"https://rickandmortyapi.com/api/character/{i}").json()
    posts.append(post)






    
