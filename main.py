import random
import time


def menu():
    print("Lets Play Dice Roller")
    time.sleep(1)
    print("Type Single for Single Player")
    time.sleep(1)
    print("Type Multi for Competitive")


menu()
time.sleep(1)
game_mode = input("Which Game Mode Would You Like to Play: ")
if game_mode.lower().strip() =="single":
    print("Single Player Chosen")
if game_mode.lower().strip() == "multi":
    print("Multiple Player Chosen")
dside = (input("Enter the number of sides on your dice: "))
while game_mode.lower().strip() == "multi":
    time.sleep(1)
    player_die = (random.randrange(1, int(dside)))
    comp_die = (random.randrange(1, int(dside)))
    print("Rolling the die ...")
    time.sleep(1)
    print("Player rolled a " + str(player_die))
    print("Computer rolled a " + str(comp_die))
    time.sleep(1)
    if player_die == comp_die:
        print("You Tied!")
    elif player_die > comp_die:
        print("You Win!")
    elif player_die < comp_die:
        print("You Lost!")
    time.sleep(1.5)
    reroll2 = input("Would you like to roll again? (Y/N)? ")
    time.sleep(.8)
    if reroll2.lower() == "n":
        raise(exit())


answer = (input("Would you like to roll the die: (Y/N) "))
while answer.lower().strip() =="y":
    player_die = (random.randrange(1, int(dside)))
    time.sleep(1)
    print("Rolling the Die...")
    time.sleep(1)
    print("You rolled a " + str(player_die))
    time.sleep(1)
    reroll = input("Would you like to roll again (Y/N) ")
    if reroll.lower() == "n":
        raise(exit())

