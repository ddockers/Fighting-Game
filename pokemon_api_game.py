import requests
<<<<<<< HEAD
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
=======
from random import randint

print('Welcome to Pokemon API battler!!!')
input('--press <ENTER> to continue--')
print('')

pokemon_select = input('Select your Pokemon with a number 1 - 151: ')
# rand_num_1 = randint(1, 151)
rand_num_2 = randint(1, 150)

pokemon_req_player = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokemon_select)
pokemon_req_cpu = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(rand_num_2))

player_poke = pokemon_req_player.json()
cpu_poke = pokemon_req_cpu.json()

print('')
print('The Player\'s Pokemon is {}, with a power level of: {}'.format(player_poke['name'],
                                                                      player_poke['base_experience']))
print('')
print('The CPU\'s Pokemon is {}, with a power level of: {}'.format(cpu_poke['name'], cpu_poke['base_experience']))
print('')
if int(player_poke['base_experience']) == int(cpu_poke['base_experience']):
    print('These Pokemon are equally matched, it\'s a draw!')
elif int(player_poke['base_experience']) > int(cpu_poke['base_experience']):
    print('Congratulations, your Pokemon beat the CPU\'s. You Win!!!')
elif int(player_poke['base_experience']) < int(cpu_poke['base_experience']):
    print('Unfortunately the CPU\'s Pokemon bested yours. Better luck next time')

print('')
input('--press <ENTER> to close--')

# print(our_poke.keys())
# print(player_poke['name'])
# print(player_poke['base_experience'])
#
# print(cpu_poke['name'])
# print(cpu_poke['base_experience'])
>>>>>>> a4b60decf67da97cd8b9dcf348c850aaba0a9442
