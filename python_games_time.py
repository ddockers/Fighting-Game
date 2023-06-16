"""
Option 1 - CLI Fighting game game:

Make a 2 player battle game, using Python!

Player selects a Character (from 5-15 options) or gets one assigned to them randomly.

If Player 2 let them pick the Character they want. If CPU assign a Character randomly.

The two Characters need to fight.

A winner must be declared via some sort of calculation.

Bonus: Want to play again?

Bonus Bonus: Make it a tournament? How far can the player go?

Note: No Pygame or Turtle allowed. CLI only.
"""

# Each char has  1 weapon, each weapon has (n)MP. Each char starts with 100HP

from random import randint

name_dict = {
    1: "Dovahkiin",
    2: "Lydia",
    3: "Astrid",
    4: "General Tulius",
    5: "Alduin",
    6: "Serana"
}
weapon_dict = {
    1: "Dragon Shout",
    2: "Burdens",
    3: "Dark Brotherhood Blade",
    4: "Imperial Greatsword",
    5: "Fire Breath",
    6: "Zombie"
}


# selection must be in range 1-6
# message: you have selected [name]

print("Welcome to the Battle for Skyrim!")
char_select_start = True

print("Here is a list of fighters")
print(name_dict)

while char_select_start:
    character_selection = input("Choose your fighter (select 1-6) ")
    if character_selection.isdigit() and int(character_selection) in range(1,7):
        print("You have chosen...")
        if int(character_selection) == 1:
            print("Dovahkiin")
        if int(character_selection) == 2:
            print("Lydia")
        if int(character_selection) == 3:
            print("Astrid")
        if int(character_selection) == 4:
            print("General Tulius")
        if int(character_selection) == 5:
            print("Alduin")
        if int(character_selection) == 6:
            print("Serana")
        char_select_start = False
    else:
        print("Invalid selection. Please choose again.")

cpu_select = True
cpu_char = randint(1,7)
while cpu_select:
    print("I have chosen...")

    if cpu_char == 1:
        print("Dovahkiin")
    if cpu_char == 2:
        print("Lydia")
    if cpu_char == 3:
        print("Astrid")
    if cpu_char == 4:
        print("General Tulius")
    if cpu_char == 5:
        print("Alduin")
    if cpu_char == 6:
        print("Serana")
    cpu_select = False

#
user_health = 100
cpu_health = 100

while char_select_start == False:
    print("Your weapon is...")
    if int(character_selection) == 1:
        user_dmg = 15
        print("Dragon Shout")
    if int(character_selection) == 2:
        user_dmg = 1
        print("Burdens")
    if int(character_selection) == 3:
        user_dmg = 8
        print("Dark Brotherhood Blade")
    if int(character_selection) == 4:
        user_dmg = 10
        print("Imperial Greatsword")
    if int(character_selection) == 5:
        user_dmg = 12
        print("Fire Breath")
    if int(character_selection) == 6:
        user_dmg = 5
        print("Zombie")
    break

while cpu_select == False:
    print("My weapon is...")
    if int(cpu_char) == 1:
        cpu_dmg = 15
        print("Dragon Shout")
    if int(cpu_char) == 2:
        cpu_dmg = 1
        print("Burdens")
    if int(cpu_char) == 3:
        cpu_dmg = 8
        print("Dark Brotherhood Blade")
    if int(cpu_char) == 4:
        cpu_dmg = 10
        print("Imperial Greatsword")
    if int(cpu_char) == 5:
        cpu_dmg = 12
        print("Fire Breath")
    if int(cpu_char) == 6:
        cpu_dmg = 5
        print("Zombie")
    break

print("Let's do battle!")



battle = True
while battle:
    while user_health >= 0 and cpu_health >= 0:
        print("Your health is " + str(user_health))
        print("My health is " + str(cpu_health))
        user_health -= cpu_dmg
        cpu_health -= user_dmg
        print(input("Press enter to continue battle"))
    if user_health < 1:
        print("I am victorious!")
        battle = False
    if cpu_health < 1:
        print("You are victorious!")
        battle = False
    else:
        battle = False



