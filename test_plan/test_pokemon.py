import requests
import pytest 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4711c95eed2eb71c3bb597edabf6c1af'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '18689'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', headers = HEADER )
    assert response.status_code == 200

def test_trainer_name():
    response_name = requests.get(url = f'{URL}/me', headers = HEADER)
    assert response_name.json()['data'][0]["trainer_name"] == 'Ayanami'

def test_my_trainer_id():
    response_name = requests.get(url = f'{URL}/trainers', headers = HEADER, params = {'trainer_id' : TRAINER_ID})
    assert response_name.json()['data'][0]["trainer_name"] == 'Ayanami'