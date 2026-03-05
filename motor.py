import feachure/inicio
import Eventos
#Motor principal

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

elif day <= 11 or health or water or food or energy or population
    print("===================================================")
    print("                     GAME OVER                     ")

    print("===================================================")
