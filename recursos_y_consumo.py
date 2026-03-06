import random

# ---------------- DIFFICULTY ----------------
difficulty = input("Choose difficulty (easy, medium, hard): ")

if difficulty == "easy":
    food = 100
    water = 100
    energy = 100
    population = random.randint(2, 6)
    health = 100
    damage = 10

    prob_min = 0.05
    prob_max = 0.1

    events = [
        "Small Supply Loss",
        "Minor Generator Glitch",
        "Short Water Leak",
        "Mild Illness",
        "Equipment Damage",
        "Cold Night"
    ]

elif difficulty == "medium":
    food = 50
    water = 50
    energy = 50
    population = random.randint(2, 6)
    health = 50
    damage = 5

    prob_min = 0.15
    prob_max = 0.3

    events = [
        "Raiders Steal Supplies",
        "Radiation Exposure",
        "Water System Failure",
        "Generator Breakdown",
        "Internal Fight",
        "Food Spoilage",
        "Medical Emergency"
    ]

elif difficulty == "hard":
    food = 20
    water = 20
    energy = 20
    population = random.randint(2, 6)
    health = 20
    damage = 3

    prob_min = 0.3
    prob_max = 0.4

    events = [
        "Armed Invasion",
        "Severe Radiation Storm",
        "Total Generator Collapse",
        "Deadly Epidemic",
        "Mass Water Contamination",
        "Structural Collapse",
        "Toxic Gas Leak"
    ]

else:
    print("Invalid difficulty")
    exit()

# ---------------- BASE CONSUMPTION ----------------
food_consumption = 0.8
water_consumption = 0.8
energy_consumption = 0.8

day = 1
days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

week_start = random.randint(0, 6)

# ---------------- GAME LOOP ----------------
while health > 0 and day <= 10:

    day_of_week = days[(week_start + day - 1) % 7]

    print("\nDay", day, "-", day_of_week)
    print("Population:", population)
    
    consumption = {
        "food": 0.8,
        "water": 0.8,
        "energy": 0.8
    }
    # weekend consumption
    if day_of_week == "saturday" or day_of_week == "sunday":
        resource = random.choice(list(consumption.keys()))
        consumption[resource] = 1.2
        print("Weekend extra consumption on:", resource)

    #  valor the diccionary
        food_consumption = consumption["food"]
        water_consumption = consumption["water"]
        energy_consumption = consumption["energy"]
    # event probability
    event_probability = random.uniform(prob_min, prob_max)

    if random.random() < event_probability:

        event = random.choice(events)
        print("Event of the day:", event)

        # (Events remain the same — no changes needed)

    # -------- DAILY CONSUMPTION --------
    total_food = population * food_consumption
    total_water = population * water_consumption
    total_energy = population * energy_consumption

    # food
    if food < total_food:
        health -= damage
        print("Not enough food. Health:", health)
    else:
        food -= total_food
        print("Remaining food:", food)

    # water
    if water < total_water:
        health -= damage
        print("Not enough water. Health:", health)
    else:
        water -= total_water
        print("Remaining water:", water)

    # energy
    if energy < total_energy:
        print("Not enough energy. Health:", health)
    else:
        energy -= total_energy
        print("Remaining energy:", energy)

    if energy <= 0:
        water = 0
        print("No energy, water system stopped working")

    print("Current health:", health)

    day += 1

# ---------------- RESULT ----------------
if health <= 0:
    print("\nThe colony has collapsed")
else:
    print("\nThe colony survived 10 days!")