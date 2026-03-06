# Random Events System Documentation

## Overview

The **Random Events System** is responsible for generating unpredictable situations that affect the survival of the population in the simulation game.

These events can:

* Reduce resources (Food, Water, Energy)
* Reduce population life
* Cause death with a certain probability

The system is designed to create **uncertainty and difficulty**, forcing players to manage their resources carefully in order to survive until the end of the simulation.

The simulation is designed to last **10 days**, and each day an event may occur depending on the game difficulty.

---

# Population System

The population is generated randomly at the start of the simulation.

```
people = random.randint(2, 6)
```

This means the simulation begins with **between 2 and 6 survivors**.

Each person shares the available resources.

---

# Resource System

The game uses three main resources:

| Resource | Description                               |
| -------- | ----------------------------------------- |
| Food     | Required for daily survival               |
| Water    | Required for hydration                    |
| Energy   | Required to operate systems and equipment |

Resources **cannot become negative**.

If a resource reaches **0**, the population will start losing life due to lack of resources.

This behavior is handled by the safe resource function:

```
def reduce_resource(resource, amount):
    if resource >= amount:
        return resource - amount
    return 0
```

This guarantees the system **never produces negative values**.

---

# Life System

Each population group has a shared **life value**.

Life decreases when certain events occur.

```
def reduce_life(amount):
    global life
    if life > amount:
        life -= amount
    else:
        life = 0
```

Life also **cannot become negative**.

---

# Death Probability System

Some events include a probability that a person dies.

```
def death_chance(probability):
    if people > 0 and random.random() < probability:
        reduce_people()
```

Example probabilities:

| Probability | Meaning                 |
| ----------- | ----------------------- |
| 0.10        | 10% chance someone dies |
| 0.30        | 30% chance someone dies |
| 0.60        | 60% chance someone dies |

This creates **risk and tension in difficult events**.

---

# Resource Consumption System

Resource consumption depends on the **day of the week**.

## Weekdays (Monday–Friday)

Each person consumes:

```
0.8 Food
0.8 Water
0.8 Energy
```

## Weekends (Saturday–Sunday)

Each person consumes:

```
1.2 Food
1.2 Water
1.2 Energy
```

This simulates **higher consumption during weekends**.

Total consumption is calculated by:

```
total_consumption = people * consumption_rate
```

---

# Event Difficulty System

The system contains **three levels of difficulty**.

Each difficulty uses a different group of random events.

---

# Easy Events (1–9)

Easy events mainly reduce resources with **low risk of death**.

Typical effects:

* Small resource losses
* Minor life damage
* Low death probability

Example effects:

* Food loss: 6–12
* Water loss: 6–12
* Energy loss: 6–12
* Life loss: 2–4
* Death probability: 10–15%

---

# Normal Events (10–18)

Normal events introduce **higher resource damage and moderate death risk**.

Typical effects:

* Resource loss: 10–18
* Life damage: 4–8
* Death probability: 25–40%

These events start to **seriously threaten the population**.

---

# Hard Events (19–27)

Hard events are **dangerous survival scenarios**.

Typical effects:

* Resource loss: 12–20
* Life damage: 6–12
* Death probability: 50–65%

In this difficulty, survival becomes extremely challenging.


