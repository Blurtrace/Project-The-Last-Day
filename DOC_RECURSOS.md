Game Variables Documentation This document explains the variables used
in the colony survival game. The variable names remain exactly the same
as they appear in the code.

1.  User Variables

user_name Type: string Description: Stores the name entered by the
player at the beginning of the game.

difficulty Type: string Description: Stores the difficulty selected by
the player (easy, medium, hard).

2.  Resource Variables

health Type: integer Description: Represents the overall health of the
colony. If it reaches 0, the game ends.

food Type: number Description: Amount of food available for the colony.
It decreases daily according to the population consumption.

water Type: number Description: Amount of water available. It decreases
daily and can also be reduced by events.

energy Type: number Description: Represents the electrical energy of the
shelter. If energy reaches 0, the water system stops working.

population Type: integer Description: Number of people living in the
colony. This value determines how many resources are consumed each day.

3.  Game Control Variables

day Type: integer Description: Tracks the current day of the game. The
game ends when day reaches 10.

days Type: list Description: A list containing the days of the week used
to simulate the passage of time in the game.

week_start Type: integer Description: Randomly selects the starting day
of the week for the game.

day_of_week Type: string Description: Stores the current day of the week
during the game loop.

4.  Consumption Variables

food_consumption Type: number Description: Amount of food each person
consumes per day.

water_consumption Type: number Description: Amount of water each person
consumes per day.

energy_consumption Type: number Description: Amount of energy each
person consumes per day.

consumption Type: dictionary Description: Dictionary introduced in the
updated version to manage resource consumption dynamically.

Example: consumption = { "food": 0.8, "water": 0.8, "energy": 0.8 }

5.  Daily Calculation Variables

total_food Type: number Description: Total food consumed by the colony
in one day. Calculated as population \* food_consumption.

total_water Type: number Description: Total water consumed in one day.
Calculated as population \* water_consumption.

total_energy Type: number Description: Total energy consumed in one day.
Calculated as population \* energy_consumption.

6.  Event Variables

events Type: list Description: List containing all possible random
events depending on the difficulty level.

event Type: string Description: Stores the randomly selected event for
the current day.

7.  Probability Variables

prob_min Type: decimal Description: Minimum probability that an event
will occur.

prob_max Type: decimal Description: Maximum probability that an event
will occur.

event_probability Type: decimal Description: Random probability value
generated between prob_min and prob_max to determine if an event occurs.

8.  Damage Variable

damage Type: integer Description: Amount of health lost when the colony
does not have enough resources.

9.  Random Module Functions

random.randint(a,b) Generates a random integer between a and b.

random.choice(list) Selects a random element from a list.

random.uniform(a,b) Generates a random decimal number between a and b.

random.random() Generates a number between 0 and 1 used for probability
checks.

11. Version Update / Code Improvements

This section explains the improvements made between the previous version
of the game and the final version implemented in recursos_y_consumo.py.

1.  Difficulty System Update The final version expands the role of
    difficulty by controlling:

-   Initial resources
-   Event probability
-   Damage received
-   Types of events available

2.  Random Population System The final version introduces a random
    population system: population = random.randint(2,6)

This allows resource consumption to vary each time the game starts.

3.  Improved Event Probability System Instead of a fixed probability,
    the system now uses probability ranges: prob_min prob_max

A random probability is generated using: random.uniform(prob_min,
prob_max)

4.  Weekend Resource Consumption System The final version introduces a
    mechanic where weekends increase resource consumption.

If the day is Saturday or Sunday, one resource is randomly selected and
its consumption increases.

Example logic: resource = random.choice(list(consumption.keys()))
consumption\[resource\] = 1.2

5.  Introduction of a Consumption Dictionary The updated version
    introduces a dictionary-based system to manage resource consumption
    dynamically, improving flexibility and code organization.

6.  Improved Day Simulation The game now simulates a weekly calendar
    using:

days =
\["monday","tuesday","wednesday","thursday","friday","saturday","sunday"\]

The starting day is randomly selected: week_start = random.randint(0,6)

7.  Resource Dependency System If energy reaches 0, the water system
    stops working:

if energy \<= 0: water = 0

This introduces dependency between resources and increases simulation
realism.

8.  Code Organization Improvements The final version reorganizes the
    code into clearer sections:

-   Difficulty configuration
-   Resource management
-   Event system
-   Game loop
-   Final result
