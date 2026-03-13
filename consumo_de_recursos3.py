import random

# ---------------- DIFICULTAD ----------------
dificultad = input("Elige dificultad (facil, media, dificil): ")

if dificultad == "facil":
    comida = 100
    agua = 100
    energia = 100
    personas = random.randint(2, 6)
    salud = 100
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
    comida = 50
    agua = 50
    energia = 50
    personas = random.randint(2, 6)
    salud = 50
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
    comida = 20
    agua = 20
    energia = 20
    personas = random.randint(2, 6)
    salud = 20
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
while salud > 0 and dia <= 10:

    dia_semana = dias[(inicio_semana + dia - 1) % 7]

    print("\nDía", dia, "-", dia_semana)
    print("Personas:", personas)

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

        # -------- FACIL --------
        if evento == "Small Supply Loss":
            perdida = random.randint(3, 6)
            comida -= perdida
            print("Se perdieron", perdida, "de comida")

        elif evento == "Minor Generator Glitch":
            perdida = random.randint(3, 5)
            energia -= perdida
            print("Se perdieron", perdida, "de energia")

        elif evento == "Short Water Leak":
            perdida = random.randint(3, 6)
            agua -= perdida
            print("Se perdieron", perdida, "de agua")

        elif evento == "Mild Illness":
            perdida = random.randint(3, 6)
            salud -= perdida
            print("Se perdieron", perdida, "de salud")

        elif evento == "Equipment Damage":
            perdida = random.randint(3, 5)
            energia -= perdida
            print("Se perdieron", perdida, "de energia")

        elif evento == "Cold Night":
            perdida = random.randint(9, 12)
            salud -= perdida
            print("Se perdieron", perdida, "de salud")

        # -------- MEDIA --------
        elif evento == "Raiders Steal Supplies":
            comida -= random.randint(4, 6)
            energia -= random.randint(2, 4)
            print("Asaltantes robaron comida y energia")

        elif evento == "Radiation Exposure":
            perdida = random.randint(1, 3)
            salud -= perdida * personas
            print("Todos perdieron", perdida, "de vida")

        elif evento == "Water System Failure":
            perdida = random.randint(4, 6)
            agua -= perdida
            print("Se perdieron", perdida, "de agua")

        elif evento == "Generator Breakdown":
            perdida = random.randint(4, 6)
            energia -= perdida
            print("Se perdieron", perdida, "de energia")

        elif evento == "Internal Fight":
            perdida = random.randint(2, 4)
            salud -= perdida
            print("Una persona perdió", perdida, "de vida")

        elif evento == "Food Spoilage":
            perdida = random.randint(4, 6)
            comida -= perdida
            print("Se perdieron", perdida, "de comida")

        elif evento == "Medical Emergency":
            perdida = random.randint(3, 5)
            salud -= perdida
            print("Una persona perdió", perdida, "de vida")

        # -------- DIFICIL --------
        elif evento == "Armed Invasion":
            comida -= random.randint(5, 10)
            energia -= random.randint(4, 8)
            print("Invasion armada! Recursos robados")

        elif evento == "Severe Radiation Storm":
            energia -= random.randint(4, 7)
            perdida = random.randint(5, 7)
            salud -= perdida * personas
            print("Tormenta radiactiva!")

        elif evento == "Total Generator Collapse":
            perdida = random.randint(8, 12)
            energia -= perdida
            print("Colapso total del generador")

        elif evento == "Deadly Epidemic":
            perdida = random.randint(7, 10)
            salud -= perdida * personas
            print("Epidemia mortal!")

        elif evento == "Mass Water Contamination":
            perdida = random.randint(6, 9)
            agua -= perdida
            print("Contaminacion del agua")

        elif evento == "Structural Collapse":
            energia -= random.randint(7, 9)
            perdida = random.randint(5, 8)
            salud -= perdida
            print("Colapso estructural")

        elif evento == "Toxic Gas Leak":
            perdida = random.randint(7, 10)
            salud -= perdida * personas
            print("Gas toxico!")

    # -------- CONSUMO DIARIO --------
    total_comida = personas * consumo_comida
    total_agua = personas * consumo_agua
    total_energia = personas * consumo_energia

    # comida
    if comida < total_comida:
        salud -= dano
        print("No hay suficiente comida. Salud:", salud)
    else:
        comida -= total_comida
        print("Comida restante:", comida)

    # agua
    if agua < total_agua:
        salud -= dano
        print("No hay suficiente agua. Salud:", salud)
    else:
        agua -= total_agua
        print("Agua restante:", agua)

    # energia
    if energia < total_energia:
        print("No hay suficiente energia. Salud:", salud)
    else:
        energia -= total_energia
        print("Energia restante:", energia)
    if energia <= 0:
        agua = 0
        print("No hay energia, el sistema de agua dejó de funcionar")                                

    print("Salud actual:", salud)

    dia += 1


# ---------------- RESULTADO ----------------
if salud <= 0:
    print("\nLa colonia ha colapsado")
else:
    print("\n¡La colonia sobrevivió 10 días!")