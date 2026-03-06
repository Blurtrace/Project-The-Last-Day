

"""
Game Initialization Module

This script:
1. Asks the player to enter a username.
2. Ensures the username is not empty using a while loop.
3. Allows the player to select a difficulty level.
4. Initializes game resources based on the selected difficulty.
"""

import random

# Ask the user to enter a username and capitalize it
user_name = input("Welcome! Please enter your UserName: ").capitalize()

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
start_day = random.choice(days)

# Keep asking until a valid username is entered
while user_name == "":
    user_name = input("You did not enter a UserName, please enter your UserName: ").capitalize()

# Boolean flag to control difficulty selection loop
select = False

# Loop until the user selects a valid difficulty option
while select != True:

    # Ask the player to choose a difficulty level
    difficult_level = input(
        f"Hi, {user_name}, select the difficulty level:\n"
        "1. Easy\n"
        "2. Medium\n"
        "3. Difficult\n"
    )

    # Easy mode configuration
    if difficult_level == "1":
        health = food = water = energy = 100
        population = random.randint(2,6)
        mode = "Easy"

       
        select = True

    # Medium mode configuration
    elif difficult_level == "2":
        health = food = water = energy = 50
        population = random.randint(2,6)
        mode = "Medium"
        
        select = True

    # Difficult mode configuration
    elif difficult_level == "3":
        health = food = water = energy = 20
        population = random.randint(2,6)
        mode = "Difficult"

        select = True

    # Invalid option handling
    else:
        print("Please, select an available option.")

# Weekend penalty
    # if start_day in ["Saturday", "Sunday"]:
    #     health -= 1.2
    #     food -= 1.2
    #     water -= 1.2
    #     energy -= 1.2

    print(
        f"\nThe game starts on: {start_day}\n"
        f"You selected {mode} mode\n"
        f"Available resources:\n"
        f"Health: {health}\n"
        f"Food: {food}\n"
        f"Water: {water}\n"
        f"Energy: {energy}\n"
        f"Population: {population}"
    )