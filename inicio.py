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
    population = 10 



  elif option == "2":
    print("Medium level selected")
    water = 50
    food = 50
    electricity = 50
    health = 50
    population = 3


  elif option == "3":
    print("Hard level selected")
    water = 20
    food = 20
    electricity = 20
    health = 20
    population = 3


  else: 
    print("Invalid option. please try again.\n")

print("population",population)
print("Resources:")
print("Water:", water)
print("Food:", food)
print("Electricity:", electricity)
print("Health:", health)