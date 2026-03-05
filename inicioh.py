import random

username = input("Enter username: ")
print("Welcome", username)

option = ""
while option not in("1","2","3"):

  option = input("Select a level for the game:\n1. Easy\n2. Medium\n3. Hard\n: ")

  if option == "1":
    print("Easy level selected")
    water = 100
    food = 100
    electricity = 100
    health = 100
    population = random.randint(2,6)
    bad_porcentage = random.uniform(0.05,0.1)



  elif option == "2":
    print("Medium level selected")
    water = 50
    food = 50
    electricity = 50
    health = 50
    population = random.randint(2,6)
    bad_porcentage = random.uniform(0.15,0.3)


  elif option == "3":
    print("Hard level selected")
    water = 20
    food = 20
    electricity = 20
    health = 20
    population = random.randint(2,6)
    bad_porcentage = random.uniform(0.3,0.4)


  else: 
    print("Invalid option. please try again.\n")
print("bad_porcentage",bad_porcentage)
print("population",population)
print("Resources:")
print("Water:", water)
print("Food:", food)
print("Electricity:", electricity)
print("Health:", health)