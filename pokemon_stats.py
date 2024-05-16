import requests
import json

def get_pokemon_stats():
    while True:
        pokemon_name = input("Please enter a Pokémon name: ").lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        response = requests.get(url)

        if response.status_code == 200:
            chosen_pokemon = response.json()
            stats = {stat['stat']['name']: stat['base_stat'] for stat in chosen_pokemon['stats']}
            print(f"Stats for {chosen_pokemon['name'].capitalize()}:")
            for stat, value in stats.items():
                print(f"{stat}: {value}")
        else:
            print("Invalid Pokémon name or Pokémon does not exist.")

        try_again = input("Would you like to try again? (yes/no): ").lower()
        if try_again != "yes":
            break


get_pokemon_stats()
