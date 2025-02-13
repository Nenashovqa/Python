import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4711c95eed2eb71c3bb597edabf6c1af'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_rename = {
    "pokemon_id": "233507",
    "name": "yellow",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": "233507"
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response.text)'''


'''response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)'''


response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)