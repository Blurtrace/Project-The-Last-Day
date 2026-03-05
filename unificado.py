import random

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

        difficult_level = input(
            f"Hi, {user_name}, select the difficulty level:\n"
            "1. Easy\n"
            "2. Medium\n"
            "3. Difficult\n"
        )

        if difficult_level == "1":
            health = food = water = energy = 100
            population = 10
            difficult_level = 1
            damage = 10

            print(
                f"You selected Easy mode\n"
                f"Available resources:\n"
                f"Health: {health}\n"
                f"Food: {food}\n"
                f"Water: {water}\n"
                f"Energy: {energy}\n"
                f"Population: {population}\n"
            )

            return health, food, water, energy, population, damage, difficult_level

        elif difficult_level == "2":
            health = food = water = energy = 50
            population = 5
            difficult_level = 2
            damage = 5

            print(
                f"You selected Medium mode\n"
                f"Available resources:\n"
                f"Health: {health}\n"
                f"Food: {food}\n"
                f"Water: {water}\n"
                f"Energy: {energy}\n"
                f"Population: {population}\n"
            )

            return health, food, water, energy, population, damage, difficult_level

        elif difficult_level == "3":
            health = food = water = energy = 20
            population = 3
            difficult_level = 3
            damage = 3

            print(
                f"You selected Difficult mode\n"
                f"Available resources:\n"
                f"Health: {health}\n"
                f"Food: {food}\n"
                f"Water: {water}\n"
                f"Energy: {energy}\n"
                f"Population: {population}\n"
            )

            return health, food, water, energy, damage, population,  difficult_level

        else:
            print("Please, select an available option.")


health, food, water, energy, population, damage, difficult_level = select_dificulty()


# recursos y consumos según dificultad
import random


comida_consumida = 1
consumo_agua = 1
consumo_energia = 1

dia = 1

while health > 0:
    
    total_comida_consumida = population * comida_consumida
    total_agua_consumida = population * consumo_agua
    total_energia_consumida = population * consumo_energia

    if food < total_comida_consumida:
        health -= damage
        print("No hay suficiente comida. Salud disminuida a", health)
    else:
        food -= total_comida_consumida
        print("Comida restante:", food)

    if water < total_agua_consumida:
        health -= damage
        print("No hay suficiente agua. Salud disminuida a", health)
    else:
        water -= total_agua_consumida
        print("Agua restante:", water)

    if energy >= total_energia_consumida:
        energy -= total_energia_consumida
        print("Energia restante:", energy)

    print("Salud actual:", health)

    dia += 1

print("\nLa colonia ha colapsado")

#-----------------------------------------------------------------------------------------
#                                 EVENTS CATEGORIZADOS
#-----------------------------------------------------------------------------------------

if difficult_level == 1:
    probabilidad = random.randint(5, 10)
    intentos_maximos = 1
    rango_eventos = 14

elif difficult_level == 2:
    probabilidad = random.randint(15, 30)
    intentos_maximos = 2
    rango_eventos = 13

elif difficult_level == 3:
    probabilidad = random.randint(30, 40)
    intentos_maximos = 3
    rango_eventos = 12

print("\nProbabilidad del dia:", probabilidad, "%")

day = 1

def eventos_random(difficultd_level, food, water, energy, health):

    eventos_activados = 0

    for intento in range(intentos_maximos):

        numero = random.randint(1, 100)

        if numero <= probabilidad:

            evento = random.randint(1, rango_eventos)

            print("\nEvent On")

            if evento == 1:
                print("Generator malfunction")
                print("Energy -15")
                energy -= 15

            elif evento == 2:
                print("Water contamination")
                print("Water -20")
                water -= 20

            elif evento == 3:
                print("Food theft")
                print("Food -15")
                food -= 15

            elif evento == 4:
                print("Structural damage")
                print("Energy -10")
                energy -= 10

            elif evento == 5:
                print("Storage leak")
                print("Water -10")
                water -= 10

            elif evento == 6:
                print("Equipment failure")
                print("Energy -8")
                energy -= 8

            elif evento == 7:
                print("Minor illness")
                print("Health -12")
                health -= 12

            elif evento == 8:
                print("Ration contamination")
                print("Food -12")
                food -= 12

            elif evento == 9:
                print("Air filtration failure")
                print("Energy -5")
                print("Health -5")
                energy -= 5
                health -= 5

            elif evento == 10:
                print("Water pump malfunction")
                print("Water -15")
                water -= 15

            elif evento == 11:
                print("Food spoilage")
                print("Food -10")
                food -= 10

            elif evento == 12:
                print("Medical supplies damaged")
                print("Health -10")
                health -= 10

            elif evento == 13:
                print("NULL EVENT - Systems stable")
                print("No resources lost")

            elif evento == 14:
                print("NULL EVENT - Calm day")
                print("No resources lost")

            eventos_activados += 1

    if eventos_activados == 0:
        print("\nNo event occurred today.")

    if food < 0:
        food = 0
    if water < 0:
        water = 0
    if energy < 0:
        energy = 0
    if health < 0:
        health = 0

    return food, water, energy, health

#===============================================================================
#                              MOTOR PRINCIPAL
#===============================================================================

while day <= 10 and health > 0:

    print("====================================================")
    print("                THE LAST DAY -", day,"              ")
    print("====================================================")

    print("\n               CURRENT STATUS                  \n")
    print("Water:", water, "| Food:", food, "Energy:", energy)
    print("Healt:", health, "| Residents:", population)


    food, water, energy, health = eventos_random(difficult_level, food, water, energy, health)


    print("\n               NEW CURRENT STATUS                  ")
    print("Water:", water, "| Food:", food, "Energy:", energy)
    print("Healt:", health, "| Residents:", population)

    day += 1
    input("\nJust press Enter or a letter or number to continue...\n")

if day == 11 and health and water and food and energy and population > 0:
    print("===================================================")
    print("    Congratulations, you survived until the 10th.  ")
    print("===================================================")

else: 
    print("===================================================")
    print("                     GAME OVER                     ")
    print("===================================================")