import random

# ---------------- DIFICULTAD ----------------
dificultad = input("Elige dificultad (facil, media, dificil): ")

if dificultad == "facil":
    food = 100
    water = 100
    energy = 100
    population = random.randint(2, 6)
    health = 100
    dano = 10

    prob_min = 0.05
    prob_max = 0.1

    eventos = [
        "Small Supply Loss",
        "Minor Generator Glitch",
        "Short Water Leak",
        "Mild Illness",
        "Equipment Damage",
        "Cold Night"
    ]

elif dificultad == "media":
    food = 50
    water = 50
    energy = 50
    population = random.randint(2, 6)
    health = 50
    dano = 5

    prob_min = 0.15
    prob_max = 0.3

    eventos = [
        "Raiders Steal Supplies",
        "Radiation Exposure",
        "Water System Failure",
        "Generator Breakdown",
        "Internal Fight",
        "Food Spoilage",
        "Medical Emergency"
    ]

elif dificultad == "dificil":
    food = 20
    water = 20
    energy = 20
    population = random.randint(2, 6)
    health = 20
    dano = 3

    prob_min = 0.3
    prob_max = 0.4

    eventos = [
        "Armed Invasion",
        "Severe Radiation Storm",
        "Total Generator Collapse",
        "Deadly Epidemic",
        "Mass Water Contamination",
        "Structural Collapse",
        "Toxic Gas Leak"
    ]

else:
    print("Dificultad no válida")
    exit()

# ---------------- CONSUMO BASE ----------------
consumo_comida = 1
consumo_agua = 1
consumo_energia = 1

dia = 1
dias = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

inicio_semana = random.randint(0, 6)

# ---------------- JUEGO ----------------
while health > 0 and dia <= 10:

    dia_semana = dias[(inicio_semana + dia - 1) % 7]

    print("\nDía", dia, "-", dia_semana)
    print("Personas:", population)

    # consumo fin de semana
    if dia_semana == "saturday" or dia_semana == "sunday":
        consumo_comida = 1.2
        consumo_agua = 1.2
        consumo_energia = 1.2
    else:
        consumo_comida = 1
        consumo_agua = 1
        consumo_energia = 1

    # probabilidad evento
    probabilidad_evento = random.uniform(prob_min, prob_max)

    if random.random() < probabilidad_evento:

        evento = random.choice(eventos)
        print("Evento del día:", evento)

        if evento == "Small Supply Loss":
            perdida = random.randint(3, 6)
            food -= perdida
            print("Se perdieron", perdida, "de comida")

        elif evento == "Minor Generator Glitch":
            perdida = random.randint(3, 5)
            energy -= perdida
            print("Se perdieron", perdida, "de energia")

        elif evento == "Short Water Leak":
            perdida = random.randint(3, 6)
            water -= perdida
            print("Se perdieron", perdida, "de agua")

        elif evento == "Mild Illness":
            perdida = random.randint(3, 6)
            health -= perdida
            print("Se perdieron", perdida, "de salud")

        elif evento == "Equipment Damage":
            perdida = random.randint(3, 5)
            energy -= perdida
            print("Se perdieron", perdida, "de energia")

        elif evento == "Cold Night":
            perdida = random.randint(9, 12)
            health -= perdida
            print("Se perdieron", perdida, "de salud")

        elif evento == "Raiders Steal Supplies":
            food -= random.randint(4, 6)
            energy -= random.randint(2, 4)
            print("Asaltantes robaron comida y energia")

        elif evento == "Radiation Exposure":
            perdida = random.randint(1, 3)
            health -= perdida * population
            print("Todos perdieron", perdida, "de vida")

        elif evento == "Water System Failure":
            perdida = random.randint(4, 6)
            water -= perdida
            print("Se perdieron", perdida, "de agua")

        elif evento == "Generator Breakdown":
            perdida = random.randint(4, 6)
            energy -= perdida
            print("Se perdieron", perdida, "de energia")

        elif evento == "Internal Fight":
            perdida = random.randint(2, 4)
            health -= perdida
            print("Una persona perdió", perdida, "de vida")

        elif evento == "Food Spoilage":
            perdida = random.randint(4, 6)
            food -= perdida
            print("Se perdieron", perdida, "de comida")

        elif evento == "Medical Emergency":
            perdida = random.randint(3, 5)
            health -= perdida
            print("Una persona perdió", perdida, "de vida")

        elif evento == "Armed Invasion":
            food -= random.randint(5, 10)
            energy -= random.randint(4, 8)
            print("Invasion armada! Recursos robados")

        elif evento == "Severe Radiation Storm":
            energy -= random.randint(4, 7)
            perdida = random.randint(5, 7)
            health -= perdida * population
            print("Tormenta radiactiva!")

        elif evento == "Total Generator Collapse":
            perdida = random.randint(8, 12)
            energy -= perdida
            print("Colapso total del generador")

        elif evento == "Deadly Epidemic":
            perdida = random.randint(7, 10)
            health -= perdida * population
            print("Epidemia mortal!")

        elif evento == "Mass Water Contamination":
            perdida = random.randint(6, 9)
            water -= perdida
            print("Contaminacion del agua")

        elif evento == "Structural Collapse":
            energy -= random.randint(7, 9)
            perdida = random.randint(5, 8)
            health -= perdida
            print("Colapso estructural")

        elif evento == "Toxic Gas Leak":
            perdida = random.randint(7, 10)
            health -= perdida * population
            print("Gas toxico!")

    # -------- CONSUMO DIARIO --------
    total_comida = population * consumo_comida
    total_agua = population * consumo_agua
    total_energia = population * consumo_energia

    # comida
    if food < total_comida:
        health -= dano
        print("No hay suficiente comida. Salud:", health)
    else:
        food -= total_comida
        print("Comida restante:", food)

    # agua
    if water < total_agua:
        health -= dano
        print("No hay suficiente agua. Salud:", health)
    else:
        water -= total_agua
        print("Agua restante:", water)

    # energia
    if energy < total_energia:
        print("No hay suficiente energia. Salud:", health)
    else:
        energy -= total_energia
        print("Energia restante:", energy)

    if energy <= 0:
        water = 0
        print("No hay energia, el sistema de agua dejó de funcionar")

    print("Salud actual:", health)

    dia += 1

# ---------------- RESULTADO ----------------
if health <= 0:
    print("\nLa colonia ha colapsado")
else:
    print("\n¡La colonia sobrevivió 10 días!")