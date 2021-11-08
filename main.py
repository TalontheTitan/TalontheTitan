import random
import time


def menu():
    print("Lets Play Dice Roller")
    time.sleep(1)
    print("Enter 1 for Single Player")
    time.sleep(1)
    print("Enter 2 for Competitive")
    time.sleep(1)
    print("Enter 0 to exit")


menu()
time.sleep(1)
game_mode = int(input("Which Game Mode Would You Like to Play: "))
while game_mode != 0:
    if game_mode == 1:
        print("Single Player Chosen")
        dside = int(input("Enter the number of sides on your dice: "))
        player_die = (random.randrange(1, int(dside)))
        time.sleep(1)
        print("Rolling the Die...")
        time.sleep(1)
        print("You rolled a " + str(player_die))
        time.sleep(1)
        reroll = input("Would you like to roll again (Y/N) ")
        if reroll.lower() == "n":
            close = input("Do you want to go back to the main menu (y/n) ")
            if close.lower().strip() == "y":
                menu()
                game_mode = int(input("Which Game Mode Would You Like to Play: "))
                x1 = input("Enter the number of sides on your dice: ")
            else:
                raise exit()
    elif game_mode == 2:
        print("Multiple Player Chosen")
        dside = int(input("Enter the number of sides on your dice: "))
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
        reroll2 = input("Would you like to roll again? (y/n)? ")
        time.sleep(.8)
        if reroll2.lower() == "n":
            close1 = input("Do you want to return to the main menu? (y/n) ")
            if close1 == "y":
                menu()
                game_mode = int(input("Which Game Mode Would You Like to Play: "))
                dside = int(input("Enter the number of sides on your dice: "))
            else:
                raise exit()
    else:
        print("Invalid Selection")
        menu()
        game_mode = int(input("Which Game Mode Would You Like to Play: "))
