import requests

url = "https://official-joke-api.appspot.com/random_joke"

def getJoke():
    response = requests.get(url)
    
    if response.status_code == 200:
        joke_data = response.json()

        print(f"{joke_data['setup']} - {joke_data['punchline']}")




getJoke()