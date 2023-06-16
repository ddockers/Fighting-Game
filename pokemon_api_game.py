import requests
from random import randint

rand_num = randint(1, 151)

pokemon_req = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(rand_num))

our_poke = pokemon_req.json()

print(our_poke['name'])
