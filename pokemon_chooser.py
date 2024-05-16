import requests
import json
import random

def player_choose_pokemon():
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=20')
    if str(response.status_code)[0] != '2':
        print("Error in requesting pokemon list")
        return False
    pokemon_list = json.loads(response.text)['results']
    pokemon_name_list = [pokemon['name'] for pokemon in pokemon_list]
    print("Here is a list of pokemon:")
    print(pokemon_name_list)
    not_chosen = True
    while not_chosen:
        pokemon_name_user = input("Please enter a pokemon or enter 'random' for a random pokemon: ").lower()
        if pokemon_name_user == "random":
            pokemon_name_user = random.choice(pokemon_name_list)
            print("Random pokemon, interesting")
            not_chosen = False
        elif pokemon_name_user in pokemon_name_list:
            print("Great choice")
            not_chosen = False
        else:
            print("Invalid pokemon")

    for pokemon in pokemon_list:
        if pokemon['name'] == pokemon_name_user:
            pokemon_url = pokemon['url']
    try:
        response2 = requests.get(pokemon_url)
    except NameError:
        print("Hmm, something went wrong with finding your pokemon")
        return False
    if str(response2.status_code)[0] != '2':
        print("Error in requesting pokemon information")
        return False
    chosen_pokemon = json.loads(response2.text)
    print(f"Your chosen pokemon is {chosen_pokemon['name'].capitalize()}")
    return chosen_pokemon

