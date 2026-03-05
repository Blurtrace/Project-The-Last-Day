Game Variables Documentation
This document explains the variables used in the colony survival game. The variable names remain exactly the same as they appear in the code.
1. User Variables
user_name
Type: string
Description: Stores the name entered by the player at the beginning of the game.
difficult_level / dificultad
Type: string
Description: Stores the difficulty selected by the player (easy, medium, difficult).
2. Resource Variables
health
Type: integer
Description: Represents the overall health of the colony. If it reaches 0, the game ends.
food
Type: number
Description: Amount of food available for the colony. It decreases daily according to the population consumption.
water
Type: number
Description: Amount of water available. It decreases daily and can also be reduced by events.
energy
Type: number
Description: Represents the electrical energy of the shelter. If energy reaches 0, the water system stops working.
population / personas
Type: integer
Description: Number of people living in the colony. This value determines how many resources are consumed each day.
3. Game Control Variables
dia
Type: integer
Description: Tracks the current day of the game. The game ends when dia reaches 10.
dias
Type: list
Description: A list containing the days of the week used to simulate the passage of time in the game.
inicio_semana
Type: integer
Description: Randomly selects the starting day of the week for the game.
dia_semana
Type: string
Description: Stores the current day of the week during the game loop.
4. Consumption Variables
consumo_comida
Type: number
Description: Amount of food each person consumes per day.
consumo_agua
Type: number
Description: Amount of water each person consumes per day.
consumo_energia
Type: number
Description: Amount of energy each person consumes per day.
5. Daily Calculation Variables
total_comida
Type: number
Description: Total food consumed by the colony in one day. Calculated as population * consumo_comida.
total_agua
Type: number
Description: Total water consumed in one day. Calculated as population * consumo_agua.
total_energia
Type: number
Description: Total energy consumed in one day. Calculated as population * consumo_energia.
6. Event Variables
eventos
Type: list
Description: List containing all possible random events depending on the difficulty level.
evento
Type: string
Description: Stores the randomly selected event for the current day.
perdida
Type: integer
Description: Represents the amount of resource or health lost during an event.
7. Probability Variables
prob_min
Type: decimal
Description: Minimum probability that an event will occur.
prob_max
Type: decimal
Description: Maximum probability that an event will occur.
probabilidad_evento
Type: decimal
Description: Random probability value generated between prob_min and prob_max to determine if an event occurs.
8. Damage Variable
dano
Type: integer
Description: Amount of health lost when the colony does not have enough resources.
9. Random Module Functions
random.randint(a,b): Generates a random integer between a and b.
random.choice(list): Selects a random element from a list.
random.uniform(a,b): Generates a random decimal number between a and b.
random.random(): Generates a number between 0 and 1 used for probability checks.
