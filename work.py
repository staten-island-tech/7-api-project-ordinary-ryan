import requests

def getPoke(poke):
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
print(pokemon)




def food(foods):
    response = requests.get(f"https://api.edamam.com/doc/open-api/nutrition-analysis-v1.yaml{foods.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    return {
        "name": data["Name"],
        "weight": data["Unit"],
        "types": [t["Unit"]["Name"] for t in data["types"]]
    }

foody = food("edamame")
print(foody)