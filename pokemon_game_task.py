from random import randint


print("Welcome to the pokemon game!")

import random

rand_num1 = randint(1,200)
rand_num2 = randint(1,200)
import requests
import json

pokemon_req1 = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(rand_num1))
pokemon_req2 = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(rand_num2))

# print(type(pokemon_req.json()))
print("OUR pokemon selected:")
our_poke = pokemon_req1.json()
print(our_poke["name"])
print(our_poke["height"])

print("CPU pokemon selected:")
cpu_poke = pokemon_req2.json()
print(cpu_poke["name"])
print(cpu_poke["height"])


our_poke_height = (our_poke["height"])
cpu_poke_height = (cpu_poke["height"])


if our_poke_height > cpu_poke_height: # if function statement 1
    print("our pokemon wins")
    # human_player_score = human_player_score + (1) # if True, print following statement
elif cpu_poke_height > our_poke_height: # if statement 2
    print("cpu pokemon wins") # if True print statement
    # cpu_player_score = cpu_player_score + (1) # increment step
else:
    print("pokemon battle ends in a draw") # else none of the above applies then both player draws
input("press enter to continue")
print("game over") # game over print statement
#print("human player score", human_player_score) # print score
#print("cpu player score", cpu_player_score)
