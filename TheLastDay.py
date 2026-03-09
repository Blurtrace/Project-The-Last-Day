import random

print("\n🌍====================================🌍")
print("          🏕️  THE LAST DAY        🏕️")
print("🌍====================================🌍")

valid_name= False

# Keep asking until a valid username is entered
while not valid_name:

    user_name = input("Welcome! Please enter your UserName: ").capitalize().strip()

    if len(user_name) <3 or len(user_name) > 15:
        print("Username must have 3 to 15 characters.")
    
    elif not user_name.replace(" ", "").isalnum():
        print("Username can only contain letters or numbers.")
    
    else:
        print("Valid username.")
        valid_name = True
   

# Boolean flag to control difficulty selection loop
select = False

while not select:

    difficult_level = input(
        f"Hi, {user_name}, select the difficulty level:\n"
        "1. Easy\n"
        "2. Medium\n"
        "3. Difficult\n"
    )

    if difficult_level == "1":
        health = food = water = energy = 100
        population = random.randint(2,6)
        mode = "Easy"
        select = True

    elif difficult_level == "2":
        health = food = water = energy = 50
        population = random.randint(2,6)
        mode = "Medium"
        select = True

    elif difficult_level == "3":
        health = food = water = energy = 20
        population = random.randint(2,6)
        mode = "Difficult"
        select = True

    else:
        print("Please, select an available option.")
        continue


    print(
        f"----------------------------\n"
        f"You selected {mode} mode\n"
        f"----------------------------\n"
        f"Available resources:\n"
        f"Health: {health}\n"
        f"Food: {food}\n"
        f"Water: {water}\n"
        f"Energy: {energy}\n"
        f"Population: {population}\n"
        f"----------------------------\n"
    )

# ---------------- DIFFICULTY SETTINGS ----------------
if difficult_level == "1":
    food = 100
    water = 100
    energy = 100
    health = 100
    health_max = 100
    damage = 10

    prob_min = 0.05
    prob_max = 0.10

elif difficult_level == "2":
    food = 50
    water = 50
    energy = 50
    health = 50
    health_max = 50
    damage = 5

    prob_min = 0.15
    prob_max = 0.30

elif difficult_level == "3":
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

    print(f"🍖 Food    [{bar(food,100)}] {max(food,0):.2f}")
    print(f"💧 Water   [{bar(water,100)}] {max(water,0):.2f}")
    print(f"⚡ Energy  [{bar(energy,100)}] {max(energy,0):.2f}")
    print(f"❤️ Health  [{bar(health,health_max)}] {max(health,0):.2f}")


# ---------------- ORIGINAL EVENTS ----------------
def random_event():

    global food, water, energy, health

    print("\n🎲 EVENT CHECK")

    event_probability = random.uniform(prob_min, prob_max)

    if random.random() > event_probability:
        print("🌙 Quiet day... nothing happened.")
        return

    if difficult_level == "1":

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

    elif difficult_level == "2":

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

    elif difficult_level == "3":

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


# ---------------- TEAM EXTRA EVENTS ----------------

def reduce_resource(resource, amount):
    if resource >= amount:
        return resource - amount
    return 0


def death_chance(probability):                              #Mary
    global population
    if population > 0 and random.random() < probability:
        population -= 1
        print("☠️ A survivor has died")


def extra_event():

    global food, water, energy, health

    event = random.randint(1,9)

    if event == 1:
        loss = random.randint(6,12)
        food = reduce_resource(food, loss)
        print(f"📦 Extra event lost {loss} food")

    elif event == 2:
        loss = random.randint(6,12)
        water = reduce_resource(water, loss)
        print(f"💧 Extra event lost {loss} water")

    elif event == 3:
        loss = random.randint(6,12)
        energy = reduce_resource(energy, loss)
        print(f"⚡ Extra event lost {loss} energy")

    elif event == 4:
        loss = random.randint(2,4)
        health -= loss
        print(f"🤒 Extra event lost {loss} health")
        death_chance(0.10)

    elif event == 5:
        loss = random.randint(3,6)
        energy = reduce_resource(energy, loss)
        health -= random.randint(1,3)
        print("⚠️ Equipment malfunction affected energy and health")
        death_chance(0.15)

    elif event == 6:
        resource = random.choice(["food","water","energy"])
        loss = random.randint(6,12)

        if resource == "food":
            food = reduce_resource(food, loss)

        elif resource == "water":
            water = reduce_resource(water, loss)

        else:
            energy = reduce_resource(energy, loss)

        print(f"🎲 Random supply loss: {loss} {resource}")

    elif event == 7:
        loss = random.randint(4,8)
        energy = reduce_resource(energy, loss)
        print(f"⚡ System instability lost {loss} energy")

    elif event == 8:
        loss = random.randint(4,8)
        water = reduce_resource(water, loss)
        print(f"💧 Water contamination lost {loss} water")

    elif event == 9:
        loss = random.randint(4,8)
        food = reduce_resource(food, loss)
        print(f"📦 Supply spoilage lost {loss} food")


# ---------------- RESOURCE CHECK ----------------
def resource_check():

    global health, water, population                               #Mary

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
    
    if health <= health_max * 0.25 and population > 1:             #Mary
        population -= 1
        print("☠️ A survivor died due to critical conditions")


# --------------------- GAME LOOP -----------------------
day = 1

while health > 0 and day <= days_total:

    weekday = days[(week_start + day - 1) % 7]

    show_status(day, weekday)

    if weekday == "Saturday" or weekday == "Sunday":
        multiplier = 1.2
        print("\n📊 Weekend consumption increased")
    
    elif weekday == "Monday" or weekday == "Tuesday":        #Mary
        multiplier = 0.8
        print("\n📊 Consumption decreased")    
    else:
        multiplier = 1

    food_cost = population * multiplier
    water_cost = population * multiplier
    energy_cost = population * multiplier

    print("\n🍽️  Daily consumption")

    food -= food_cost
    energy = energy_cost

    if energy > 0:                                          #Mary
        water -= water_cost
    else:
        print("🚱 No energy → water cannot be consumed")   

    print(f"➖ Food -{food_cost:.2f}")
    print(f"➖ Energy -{energy_cost:.2f}")
    print(f"➖ Water -{water_cost:.2f}")              #Mary


    random_event()

    if random.random() < 0.25:
        extra_event()

    resource_check()

    input("Press enter for continue..")                  #Mary

    day += 1


# ---------------- RESULT ----------------
if health <= 0 or population <= 0:                       #Mary

    print("\n☠️====================================☠️")
    print("            COLONY COLLAPSED")
    print("☠️====================================☠️")

else:

    print("\n🏆====================================🏆")
    print("       THE COLONY SURVIVED 10 DAYS")
    print("🏆====================================🏆")