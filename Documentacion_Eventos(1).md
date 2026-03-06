# Random Events System
### Survival to Extrema

---

The **Random Events System** generates unexpected situations during the game that affect the survival of the population.

These events simulate environmental problems, system failures, and survival challenges that may reduce resources, damage life, or cause the death of people.

Events occur randomly and are divided into **three difficulty levels** to control the intensity of the game.

---

## Event Structure

The system is divided into three groups based on difficulty.

| Difficulty | Event Range |
|------------|-------------|
| Easy | 1 – 9 |
| Normal | 10 – 18 |
| Hard | 19 – 27 |

Each group contains events with different levels of impact on the resources and population.

---

## Resources Affected

Random events can affect the following game resources:

- 🍖 **Food** – Supplies required to feed the population
- 💧 **Water** – Essential survival resource
- ⚡ **Energy** – Required for system operations
- ❤️ **Life** – Represents the health status of the group
- 👥 **People** – Number of survivors in the game

The system ensures that **resources never become negative**.

---

## Resource Protection System

To prevent negative values, the following function is used:

```python
def reduce_resource(resource, amount):
    if resource >= amount:
        return resource - amount
    return 0
