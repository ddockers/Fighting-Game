import requests
import json
from random import randint


print("Welcome to Super Pokemon Pokebattle to the Pokedeath!")
player_poke_select = input("Select a Pokemon from the Pokedex using their Pokedex number 1 - 151 ")
pokedex_num = randint(1, 151)

cpu_pokemon_req = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(pokedex_num)) # This gives the pokedex of the pokemon, according to the pokedata
player_poke_req = requests.get('https://pokeapi.co/api/v2/pokemon/' + player_poke_select)

cpu_poke = cpu_pokemon_req.json()
player_poke = player_poke_req.json()
#print(cpu_poke['name']) # name connected to pokedex num
#print(cpu_poke.keys())
# print(cpu_poke['base_experience'])




print("You have selected " + (player_poke['name']))
print(' ')
print("Your base XP is " + str(player_poke['base_experience']))
input("Press Enter to continue")
print(' ')
print("I have selected " + cpu_poke['name'])
print(' ')
print("My base XP is " + str(cpu_poke['base_experience']))
input("Press Enter to continue")
print("Let's Pokebattle to the Pokedeath!")
input("Press Enter to continue")
if int(player_poke['base_experience']) == int(cpu_poke['base_experience']):
    print("Oh dear. Both Pokemon are Pokedead")
elif int(player_poke['base_experience']) > int(cpu_poke['base_experience']):
    print("Congratulations, your Pokemon beat the Opponent to Pokedeath")
elif int(player_poke['base_experience']) < int(cpu_poke['base_experience']):
    print("You are Pokedead")