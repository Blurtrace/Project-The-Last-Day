import random

print("\n🌍====================================🌍")
print("        🏕️  SURVIVAL COLONY GAME  🏕️")
print("🌍====================================🌍")

difficulty = input("\nChoose difficulty (easy, medium, hard): ")

# ---------------- POPULATION RANDOM ----------------
population = random.randint(2,6)

# ---------------- DIFFICULTY SETTINGS ----------------
if difficulty == "easy":
    food = 100
    water = 100
    energy = 100
    health = 100
    health_max = 100
    damage = 10

    prob_min = 0.05
    prob_max = 0.10

elif difficulty == "medium":
    food = 50
    water = 50
    energy = 50
    health = 50
    health_max = 50
    damage = 5

    prob_min = 0.15
    prob_max = 0.30

elif difficulty == "hard":
    food = 20
    water = 20
    energy = 20
    health = 20
    health_max = 20
    damage = 3

    prob_min = 0.30
    prob_max = 0.40

else:
    print("Invalid difficulty")
    exit()

days_total = 10


# ---------------- WEEK SYSTEM ----------------
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

week_start = random.randint(0,6)


# ---------------- VISUAL BARS ----------------
def bar(value, maximum):

    if value < 0:
        value = 0

    size = 10
    filled = int((value / maximum) * size)
    empty = size - filled

    return "█" * filled + "░" * empty


# ---------------- INTERFACE ----------------
def show_status(day, weekday):

    print("\n📅====================================📅")
    print(f"        DAY {day}  |  {weekday}")
    print("📅====================================📅")

    print(f"👥 Population: {population}")

    print(f"🍖 Food    [{bar(food,100)}] {food}")
    print(f"💧 Water   [{bar(water,100)}] {water}")
    print(f"⚡ Energy  [{bar(energy,100)}] {energy}")
    print(f"❤️ Health  [{bar(health,health_max)}] {health}")


# ---------------- EVENTS ----------------
def random_event():

    global food, water, energy, health

    print("\n🎲 EVENT CHECK")

    event_probability = random.uniform(prob_min, prob_max)

    if random.random() > event_probability:
        print("🌙 Quiet day... nothing happened.")
        return

    if difficulty == "easy":

        event = random.choice([
            "Small Supply Loss",
            "Minor Generator Glitch",
            "Short Water Leak",
            "Mild Illness",
            "Equipment Damage",
            "Cold Night"
        ])

        print("⚠️ Event:", event)

        if event == "Small Supply Loss":
            loss = random.randint(2,4)
            food -= loss
            print(f"📦 Lost {loss} food")

        elif event == "Minor Generator Glitch":
            loss = random.randint(2,3)
            energy -= loss
            print(f"⚡ Lost {loss} energy")

        elif event == "Short Water Leak":
            loss = random.randint(2,4)
            water -= loss
            print(f"💧 Lost {loss} water")

        elif event == "Mild Illness":
            loss = random.randint(1,2)
            health -= loss
            print(f"🤒 Survivor lost {loss} health")

        elif event == "Equipment Damage":
            loss = random.randint(2,4)
            energy -= loss
            print(f"🔧 Lost {loss} energy")

        elif event == "Cold Night":
            health -= 1
            print("🥶 Everyone lost 1 health")


    elif difficulty == "medium":

        event = random.choice([
            "Raiders Steal Supplies",
            "Radiation Exposure",
            "Water System Failure",
            "Generator Breakdown",
            "Internal Fight",
            "Food Spoilage",
            "Medical Emergency"
        ])

        print("⚠️ Event:", event)

        if event == "Raiders Steal Supplies":
            food -= random.randint(4,6)
            energy -= random.randint(2,4)

        elif event == "Radiation Exposure":
            health -= random.randint(1,3)

        elif event == "Water System Failure":
            water -= random.randint(4,6)

        elif event == "Generator Breakdown":
            energy -= random.randint(4,6)

        elif event == "Internal Fight":
            health -= random.randint(2,4)

        elif event == "Food Spoilage":
            food -= random.randint(4,6)

        elif event == "Medical Emergency":
            health -= random.randint(3,5)


    elif difficulty == "hard":

        event = random.choice([
            "Armed Invasion",
            "Severe Radiation Storm",
            "Total Generator Collapse",
            "Deadly Epidemic",
            "Mass Water Contamination",
            "Structural Collapse",
            "Toxic Gas Leak"
        ])

        print("⚠️ Event:", event)

        if event == "Armed Invasion":
            food -= random.randint(5,8)
            energy -= random.randint(4,6)

        elif event == "Severe Radiation Storm":
            energy -= random.randint(3,5)
            health -= random.randint(2,4)

        elif event == "Total Generator Collapse":
            energy -= random.randint(6,9)

        elif event == "Deadly Epidemic":
            health -= random.randint(3,5)

        elif event == "Mass Water Contamination":
            water -= random.randint(5,8)

        elif event == "Structural Collapse":
            energy -= random.randint(4,7)
            health -= random.randint(3,5)

        elif event == "Toxic Gas Leak":
            health -= random.randint(2,4)


# ---------------- RESOURCE CHECK ----------------
def resource_check():

    global health, water

    damage_total = 0

    if food <= 0:
        damage_total += damage
        print("🚨 NO FOOD")

    water_available = water

    if energy <= 0:
        water_available = 0
        print("⚠️ No energy → water pumps stopped")

    if water_available <= 0:
        damage_total += damage
        print("🚨 NO WATER")

    if energy <= 0:
        damage_total += damage
        print("🚨 NO ENERGY")

    if damage_total > 0:
        health -= damage_total
        print(f"💔 Colony lost {damage_total} health")


# ---------------- GAME LOOP ----------------
day = 1

while health > 0 and day <= days_total:

    weekday = days[(week_start + day - 1) % 7]

    show_status(day, weekday)

    # WEEKEND CONSUMPTION
    if weekday == "Saturday" or weekday == "Sunday":
        multiplier = 1.2
        print("\n📊 Weekend consumption increased")
    else:
        multiplier = 1

    food_cost = population * multiplier
    water_cost = population * multiplier
    energy_cost = population * multiplier

    print("\n🍽️ Daily consumption")

    food -= food_cost
    water -= water_cost
    energy -= energy_cost

    print(f"➖ Food -{food_cost}")
    print(f"➖ Water -{water_cost}")
    print(f"➖ Energy -{energy_cost}")

    random_event()

    resource_check()

    day += 1


# ---------------- RESULT ----------------
if health <= 0:

    print("\n☠️====================================☠️")
    print("            COLONY COLLAPSED")
    print("☠️====================================☠️")

else:

    print("\n🏆====================================🏆")
    print("       THE COLONY SURVIVED 10 DAYS")
    print("🏆====================================🏆")