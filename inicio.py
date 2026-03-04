

"""
Game Initialization Module

This script:
1. Asks the player to enter a username.
2. Ensures the username is not empty using a while loop.
3. Allows the player to select a difficulty level.
4. Initializes game resources based on the selected difficulty.
"""

# Ask the user to enter a username and capitalize it
user_name = input("Welcome! Please enter your UserName: ").capitalize()

# Keep asking until a valid username is entered
while user_name == "":
    user_name = input("You did not enter a UserName, please enter your UserName: ").capitalize()

# Loop until the user selects a valid difficulty option
def select_dificulty():
    select = False # Boolean flag to control difficulty selection loop
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
            population = 10
            bad_porcentage = 20

            print(
                f"You selected Easy mode\n"
                f"Available resources:\n"
                f"Health: {health}\n"
                f"Food: {food}\n"
                f"Water: {water}\n"
                f"Energy: {energy}\n"
                f"Population: {population}"
                f"Bad Porcentage: {bad_porcentage}"
            )

            select = True

        # Medium mode configuration
        elif difficult_level == "2":
            health = food = water = energy = 50
            population = 5
            bad_porcentage = 40

            print(
                f"You selected Medium mode\n"
                f"Available resources:\n"
                f"Health: {health}\n"
                f"Food: {food}\n"
                f"Water: {water}\n"
                f"Energy: {energy}\n"
                f"Population: {population}"
                f"Bad Porcentage: {bad_porcentage}"
            )

            select = True

        # Difficult mode configuration
        elif difficult_level == "3":
            health = food = water = energy = 20
            population = 3
            bad_porcentage = 60

            print(
                f"You selected Difficult mode\n"
                f"Available resources:\n"
                f"Health: {health}\n"
                f"Food: {food}\n"
                f"Water: {water}\n"
                f"Energy: {energy}\n"
                f"Population: {population}"
                f"Bad Porcentage: {bad_porcentage}"
            )

            select = True

        # Invalid option handling
        else:
            print("Please, select an available option.")
        return
select_dificulty()