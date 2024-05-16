import requests
import json
import random

def get_pokemon_stats(pokemon_name):
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    except requests.exceptions.RequestException as e:
        print("Error in requesting pokemon information:", e)
        return False

    if response.status_code != 200:
        print("Error in requesting pokemon information")
        return False

    pokemon_data = json.loads(response.text)
    stats = pokemon_data['stats']
    pokemon_stats = {}
    for stat in stats:
        stat_name = stat['stat']['name']
        base_stat = stat['base_stat']
        pokemon_stats[stat_name] = base_stat
    return pokemon_stats

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


    pokemon_stats = get_pokemon_stats(chosen_pokemon['name'])
    if pokemon_stats:
        print(f"Stats for {chosen_pokemon['name'].capitalize()}:")
        for stat_name, stat_value in pokemon_stats.items():
            print(f"{stat_name.capitalize()}: {stat_value}")
        return True
    else:
        return False

player_choose_pokemon()