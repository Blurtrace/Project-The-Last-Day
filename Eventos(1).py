import random

people = random.randint(2, 6)

# ==============================
# SAFE FUNCTIONS (NO NEGATIVES)
# ==============================

def reduce_resource(resource, amount):
    if resource >= amount:
        return resource - amount
    return 0

def reduce_life(amount):
    global life
    if life > amount:
        life -= amount
    else:
        life = 0

def reduce_people():
    global people
    if people > 0:
        people -= 1

def death_chance(probability):
    if people > 0 and random.random() < probability:
        reduce_people()

# ==============================
# EASY EVENTS (1–9)
# ==============================

def easy_random_event():
    global food, water, energy

    event = random.randint(1, 9)

    if event == 1:
        food = reduce_resource(food, random.randint(6, 12))

    elif event == 2:
        water = reduce_resource(water, random.randint(6, 12))

    elif event == 3:
        energy = reduce_resource(energy, random.randint(6, 12))

    elif event == 4:
        reduce_life(random.randint(2, 4))
        death_chance(0.10)

    elif event == 5:
        energy = reduce_resource(energy, random.randint(6, 12))
        reduce_life(random.randint(2, 4))
        death_chance(0.15)

    elif event == 6:
        resource = random.choice(["food", "water", "energy"])
        loss = random.randint(6, 12)

        if resource == "food":
            food = reduce_resource(food, loss)
        elif resource == "water":
            water = reduce_resource(water, loss)
        else:
            energy = reduce_resource(energy, loss)

    elif event == 7:
        energy = reduce_resource(energy, random.randint(6, 12))

    elif event == 8:
        water = reduce_resource(water, random.randint(6, 12))

    elif event == 9:
        food = reduce_resource(food, random.randint(6, 12))

# ==============================
# NORMAL EVENTS (10–18)
# ==============================

def normal_random_event():
    global food, water, energy

    event = random.randint(10, 18)

    if event == 10:
        loss = random.randint(10, 18)
        if random.choice([True, False]):
            food = reduce_resource(food, loss)
        else:
            energy = reduce_resource(energy, loss)
        death_chance(0.25)

    elif event == 11:
        reduce_life(random.randint(4, 8))
        death_chance(0.30)

    elif event == 12:
        water = reduce_resource(water, random.randint(10, 18))

    elif event == 13:
        energy = reduce_resource(energy, random.randint(10, 18))

    elif event == 14:
        reduce_life(random.randint(4, 8))
        death_chance(0.35)

    elif event == 15:
        food = reduce_resource(food, random.randint(10, 18))

    elif event == 16:
        reduce_life(random.randint(4, 8))
        death_chance(0.30)

    elif event == 17:
        energy = reduce_resource(energy, random.randint(10, 18))
        reduce_life(random.randint(3, 6))
        death_chance(0.40)

    elif event == 18:
        energy = reduce_resource(energy, random.randint(10, 18))

# ==============================
# HARD EVENTS (19–27)
# ==============================

def hard_random_event():
    global food, water, energy

    event = random.randint(19, 27)

    if event == 19:
        loss = random.randint(12, 20)
        if random.choice([True, False]):
            food = reduce_resource(food, loss)
        else:
            energy = reduce_resource(energy, loss)
        death_chance(0.50)

    elif event == 20:
        reduce_life(random.randint(6, 12))
        death_chance(0.60)

    elif event == 21:
        energy = reduce_resource(energy, random.randint(12, 20))
        death_chance(0.50)

    elif event == 22:
        reduce_life(random.randint(6, 12))
        death_chance(0.60)

    elif event == 23:
        water = reduce_resource(water, random.randint(12, 20))

    elif event == 24:
        if random.choice([True, False]):
            energy = reduce_resource(energy, random.randint(12, 20))
        else:
            reduce_life(random.randint(6, 12))
        death_chance(0.55)

    elif event == 25:
        reduce_life(random.randint(6, 12))
        death_chance(0.60)

    elif event == 26:
        reduce_life(random.randint(6, 12))
        death_chance(0.65)

    elif event == 27:
        loss = random.randint(12, 20)
        if random.choice([True, False]):
            food = reduce_resource(food, loss)
        else:
            energy = reduce_resource(energy, loss)
        death_chance(0.55)