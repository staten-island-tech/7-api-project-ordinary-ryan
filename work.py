import requests

""" def getPoke(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

pokemon = getPoke("Bulbasaur")
print(pokemon)  """


def dog(dogs):
    url = "https://dogapi.dog/api/v2/breeds"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    print(data)
    return {
        'attributes': {
            "name": data['name'],
            "description" : data['description']
        }
    }
doggy = dog("Afghan Hound")
print(doggy) 
dog(doggy)

""" doggy = {
    "name": "Afghan Hound",
    "type": "breed",
    "description" : "The Afghan Hound is a large and elegant breed of dog that was originally bred in Afghanistan for hunting small game. They are intelligent, independent, and athletic, and make excellent companion dogs."
}

doggy = dog("Afghan Hound")
for key, value in doggy:
    print(key, "→", value)
 """ 