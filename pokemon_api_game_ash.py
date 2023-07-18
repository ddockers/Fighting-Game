import requests
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
print('The Player\'s Pokemon is {}, with a power level of: {}'.format(player_poke['name'], player_poke['base_experience']))
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