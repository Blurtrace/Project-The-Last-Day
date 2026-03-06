import inicio
import Eventos
import random
#Motor principal

#===============================================================================
#                              MOTOR PRINCIPAL
#===============================================================================

day = 1
days_weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
start_week = random.randint(0,6)

while day <= 10 and health > 0:

    current_day = days_weeks[(start_week + day) % 7]

    print("=======================================================")
    print("             THE LAST DAY -", current_day, day,"       ")
    print("=======================================================")

    print("\n               CURRENT STATUS                  \n")
    print("Healt:", health, "| Food:", food, "| Water:", water, "Energy:", energy, "| Population:", population)

#---------------------------------------------------------------------------------------------------------------
#  Esto aplica los eventos en los transcursos del dia
    
    food, water, energy, health = eventos_random(food, water, energy, health)
#---------------------------------------------------------------------------------------------------------------
    day += 1

    print("\n               NEW CURRENT STATUS                  \n")
    print("Healt:", health, "| Food:", food, "| Water:", water, "Energy:", energy, "| Population:", population)

    
    input("Just press Enter or a letter or number to continue...\n")

if day == 11 and health and population > 0:
    print("======================================================")
    print("    Congratulations, you survived until the 10th.     ")
    print("======================================================")

else:
    print("======================================================")
    print("                     GAME OVER                        ")
    print("======================================================")

