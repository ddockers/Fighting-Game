import requests
from random import randint

rand_num_1 = randint(1, 151)
rand_num_2 = randint(1, 150)

pokemon_req_player = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(rand_num_1))
pokemon_req_cpu = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(rand_num_2))

player_poke = pokemon_req_player.json()
cpu_poke = pokemon_req_cpu.json()

# print(our_poke.keys())
print(player_poke['name'])
print(player_poke['base_experience'])

print(cpu_poke['name'])
print(cpu_poke['base_experience'])
