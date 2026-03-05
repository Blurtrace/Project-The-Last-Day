# recursos y consumos según dificultad
import random

dificultad = input("Elige dificultad (facil, media, dificil): ")

if dificultad == "facil":
    comida = 100
    agua = 100
    energia = 100
    personas = random.randint(2, 6)
    salud = 100
    dano = 10
    probabilidad_evento = random.uniform(0.05, 0.1)

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
    probabilidad_evento = random.uniform(0.15, 0.3)

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
    probabilidad_evento = random.uniform(0.3, 0.4)

    eventos = [#eventos
        "Armed Invasion",
        "Severe Radiation Storm",
        "Total Generator Collapse",
        "Deadly Epidemic",
        "Mass Water Contamination",
        "Structural Collapse",
        "Toxic Gas Leak"
    ]

comida_consumida = 1
consumo_agua = 1
consumo_energia = 1

dia = 1

while salud > 0:

    print("\nDía", dia)

    if random.random() < probabilidad_evento:
        evento = random.choice(eventos)
        print("Evento del dia:", evento)

        # ---------------- MODO FACIL ----------------
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

        # ---------------- MODO NORMAL ----------------
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

        # ---------------- MODO DIFICIL ----------------
        elif evento == "Armed Invasion":
            comida -= random.randint(5, 10)
            energia -= random.randint(4, 8)
            print("Invasion armada! Recursos robados")

        elif evento == "Severe Radiation Storm":
            energia -= random.randint(4, 7)
            perdida = random.randint(5, 7)
            salud -= perdida * personas
            print("Tormenta radiactiva! Todos pierden", perdida, "de vida")

        elif evento == "Total Generator Collapse":
            perdida = random.randint(8, 12)
            energia -= perdida
            print("Colapso total del generador. Se perdieron", perdida, "de energia")

        elif evento == "Deadly Epidemic":
            perdida = random.randint(7, 10)
            salud -= perdida * personas
            print("Epidemia mortal! Todos pierden", perdida, "de vida")

        elif evento == "Mass Water Contamination":
            perdida = random.randint(6, 9)
            agua -= perdida
            print("Contaminacion masiva del agua")

        elif evento == "Structural Collapse":
            energia -= random.randint(7, 9)
            perdida = random.randint(5, 8)
            salud -= perdida
            print("Colapso estructural! Una persona perdió", perdida, "de vida")

        elif evento == "Toxic Gas Leak":
            perdida = random.randint(7, 10)
            salud -= perdida * personas
            print("Fuga de gas toxico! Todos pierden", perdida, "de vida")

    # ---------------- CONSUMO DIARIO ----------------
    total_comida_consumida = personas * comida_consumida
    total_agua_consumida = personas * consumo_agua
    total_energia_consumida = personas * consumo_energia

    if comida < total_comida_consumida:
        salud -= dano
        print("No hay suficiente comida. Salud disminuida a", salud)
    else:
        comida -= total_comida_consumida
        print("Comida restante:", comida)

    if agua < total_agua_consumida:
        salud -= dano
        print("No hay suficiente agua. Salud disminuida a", salud)
    else:
        agua -= total_agua_consumida
        print("Agua restante:", agua)

    if energia >= total_energia_consumida:
        energia -= total_energia_consumida
        print("Energia restante:", energia)

    print("Salud actual:", salud)

    dia += 1

print("\nLa colonia ha colapsado")