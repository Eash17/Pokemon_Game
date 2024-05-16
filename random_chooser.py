import requests
import json
import random

def player_choose_pokemon():
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=20')
    pokemon_list = json.loads(response.text)['results']
    pokemon_name_list = [pokemon['name'] for pokemon in pokemon_list]
    print("Here is a list of pokemon")
    print(pokemon_name_list)
    not_chosen = True
    while not_chosen:
        pokemon_name_user = input("Please enter a Pokémon: ").lower()
        if pokemon_name_user in pokemon_name_list:
            print("Great choice!")
            not_chosen = False
        else:
            print("Invalid Pokémon name. Please try again.")

    for pokemon in pokemon_list:
        if pokemon['name'] == pokemon_name_user:
            pokemon_url = pokemon['url']
    print("You will be battling against...")
    response2 = requests.get(pokemon_url)
    chosen_pokemon = json.loads(response2.text)
    return chosen_pokemon

def cpu_choose_pokemon():
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=20')
    pokemon_list = json.loads(response.text)['results']
    random_pokemon = random.choice(pokemon_list)
    print(f"{random_pokemon['name'].capitalize()}!")

    return random_pokemon


def main():
    player_pokemon = player_choose_pokemon()
    cpu_pokemon = cpu_choose_pokemon()

if __name__ == "__main__":
    main()
