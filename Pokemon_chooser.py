import requests
import json

def player_choose_pokemon():
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
    pokemon_list = json.loads(response.text)['results']
    pokemon_name_list = [pokemon['name'] for pokemon in pokemon_list]
    not_chosen = True
    while not_chosen:
        pokemon_name_user = input("Please enter a pokemon: ").lower()
        if pokemon_name_user in pokemon_name_list:
            print("Great Choice")
            not_chosen = False
        else:
            print("Invalid pokemon")

    for pokemon in pokemon_list:
        if pokemon['name'] == pokemon_name_user:
            pokemon_url = pokemon['url']
    print(pokemon_url)
    response2 = requests.get(pokemon_url)
    chosen_pokemon = json.loads(response2.text)
    return chosen_pokemon

print(player_choose_pokemon())