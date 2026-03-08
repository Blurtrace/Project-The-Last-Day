

"""
Game Initialization Module

Autor: Luisa de la Rosa and Hillary Yepes Glen
This script:
1. Asks the player to enter a username.
2. Ensures the username is not empty using a while loop.
3. Allows the player to select a difficulty level.
4. Initializes game resources based on the selected difficulty.
"""



import random

valid_name= False

# Keep asking until a valid username is entered
while not valid_name:

    # Ask the user to enter a username and capitalize it
    user_name = input("Welcome! Please enter your UserName: ").capitalize().strip()

    if len(user_name) <3 or len(user_name) > 15:
        print("Username must have 3 to 15 characters.")
    
    elif not user_name.replace(" ", "").isalnum():
        print("Username can only contain letters or numbers.")
    
    else:
        print("Valid username.")
        valid_name = True
   

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
start_day = random.choice(days)



# Boolean flag to control difficulty selection loop
select = False

# Loop until the user selects a valid difficulty option
while not select:

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
        continue

# Weekend penalty
    # if start_day in ["Saturday", "Sunday"]:
    #     health -= 1.2
    #     food -= 1.2
    #     water -= 1.2
    #     energy -= 1.2

    print(
        f"----------------------------\n"
        f"You selected {mode} mode\n"
        f"----------------------------\n"
        f"The game starts on: {start_day}\n"
        f"----------------------------\n"
        f"Available resources:\n"
        f"Health: {health}\n"
        f"Food: {food}\n"
        f"Water: {water}\n"
        f"Energy: {energy}\n"
        f"Population: {population}\n"
        f"----------------------------\n"
    )