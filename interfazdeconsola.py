import random

print("\n🌍====================================🌍")
print("        🏕️  JUEGO DE SUPERVIVENCIA  🏕️")
print("🌍====================================🌍")

nivel = input("\nSelecciona dificultad (facil / medio / dificil): ").lower()

# POBLACIÓN RANDOM
personas = random.randint(2,6)

# CONFIGURACIÓN SEGÚN NIVEL
if nivel == "facil":
    comida = 100
    agua = 100
    energia = 100
    daño_recurso = 10
    vida = 100
    vida_max = 100
    prob_min = 5
    prob_max = 10

elif nivel == "medio":
    comida = 50
    agua = 50
    energia = 50
    daño_recurso = 5
    vida = 50
    vida_max = 50
    prob_min = 15
    prob_max = 30

elif nivel == "dificil":
    comida = 20
    agua = 20
    energia = 20
    daño_recurso = 3
    vida = 20
    vida_max = 20
    prob_min = 30
    prob_max = 40

dias = 10


# BARRAS VISUALES
def barra(valor, maximo):

    if valor < 0:
        valor = 0

    tamaño = 10
    llenos = int((valor / maximo) * tamaño)
    vacios = tamaño - llenos

    return "█" * llenos + "░" * vacios


# INTERFAZ
def mostrar_estado(dia):

    print("\n📅====================================📅")
    print(f"              DÍA {dia}")
    print("📅====================================📅")

    print(f"👥 Sobrevivientes: {personas}")

    print(f"🍖 Comida   [{barra(comida,100)}] {comida}")
    print(f"💧 Agua     [{barra(agua,100)}] {agua}")
    print(f"⚡ Energía  [{barra(energia,100)}] {energia}")
    print(f"❤️ Salud    [{barra(vida,vida_max)}] {vida}")


# CONSUMO DIARIO
def consumo_diario():
    global comida, agua, energia

    comida -= personas
    agua -= personas
    energia -= personas

    print("\n🍽️ Consumo diario")
    print(f"➖ {personas} comida")
    print(f"➖ {personas} agua")
    print(f"➖ {personas} energía")


# EVENTOS RANDOM
def evento_random():
    global comida, agua, energia, vida

    print("\n🎲 EVENTO DEL DÍA")

    probabilidad = random.randint(1,100)
    prob_evento = random.randint(prob_min, prob_max)

    if probabilidad > prob_evento:
        print("🌙 Día tranquilo... no ocurrió ningún evento.")
        return


    if nivel == "facil":

        evento = random.choice([
            "comida","energia","agua","enfermedad","equipo","frio"
        ])

        if evento == "comida":
            perdida = random.randint(2,4)
            comida -= perdida
            print(f"📦 Small Supply Loss → -{perdida} comida")

        elif evento == "energia":
            perdida = random.randint(2,3)
            energia -= perdida
            print(f"⚡ Minor Generator Glitch → -{perdida} energía")

        elif evento == "agua":
            perdida = random.randint(2,4)
            agua -= perdida
            print(f"💧 Short Water Leak → -{perdida} agua")

        elif evento == "enfermedad":
            perdida = random.randint(1,2)
            vida -= perdida
            print(f"🤒 Mild Illness → -{perdida} salud")

        elif evento == "equipo":
            perdida = random.randint(2,4)
            energia -= perdida
            print(f"🔧 Equipment Damage → -{perdida} energía")

        elif evento == "frio":
            vida -= 1
            print("🥶 Cold Night → Todos pierden 1 salud")


    elif nivel == "medio":

        evento = random.choice([
            "saqueadores","radiacion","agua","generador",
            "pelea","comida","medico"
        ])

        if evento == "saqueadores":
            comida -= random.randint(4,6)
            energia -= random.randint(2,4)
            print("⚔️ Raiders Steal Supplies")

        elif evento == "radiacion":
            perdida = random.randint(1,3)
            vida -= perdida
            print(f"☢️ Radiation Exposure → -{perdida} salud")

        elif evento == "agua":
            perdida = random.randint(4,6)
            agua -= perdida
            print(f"💧 Water System Failure → -{perdida} agua")

        elif evento == "generador":
            perdida = random.randint(4,6)
            energia -= perdida
            print(f"⚡ Generator Breakdown → -{perdida} energía")

        elif evento == "pelea":
            perdida = random.randint(2,4)
            vida -= perdida
            print(f"🥊 Internal Fight → -{perdida} salud")

        elif evento == "comida":
            perdida = random.randint(4,6)
            comida -= perdida
            print(f"🍖 Food Spoilage → -{perdida} comida")

        elif evento == "medico":
            perdida = random.randint(3,5)
            vida -= perdida
            print(f"🚑 Medical Emergency → -{perdida} salud")


    elif nivel == "dificil":

        evento = random.choice([
            "invasion","radiacion","generador","epidemia",
            "agua","derrumbe","gas"
        ])

        if evento == "invasion":
            comida -= random.randint(5,8)
            energia -= random.randint(4,6)
            print("💀 Armed Invasion")

        elif evento == "radiacion":
            energia -= random.randint(3,5)
            vida -= random.randint(2,4)
            print("☢️ Severe Radiation Storm")

        elif evento == "generador":
            perdida = random.randint(6,9)
            energia -= perdida
            print(f"⚡ Total Generator Collapse → -{perdida} energía")

        elif evento == "epidemia":
            perdida = random.randint(3,5)
            vida -= perdida
            print(f"🦠 Deadly Epidemic → -{perdida} salud")

        elif evento == "agua":
            perdida = random.randint(5,8)
            agua -= perdida
            print(f"💧 Mass Water Contamination → -{perdida} agua")

        elif evento == "derrumbe":
            energia -= random.randint(4,7)
            vida -= random.randint(3,5)
            print("🏚️ Structural Collapse")

        elif evento == "gas":
            perdida = random.randint(2,4)
            vida -= perdida
            print(f"☣️ Toxic Gas Leak → -{perdida} salud")


# VERIFICAR RECURSOS
def verificar_recursos():
    global vida

    daño = 0

    if comida <= 0:
        daño += daño_recurso
        print("🚨 SIN COMIDA")

    agua_disponible = agua

    if energia <= 0:
        agua_disponible = 0
        print("⚠️ Sin energía la bomba de agua no funciona")

    if agua_disponible <= 0:
        daño += daño_recurso
        print("🚨 SIN AGUA")

    if energia <= 0:
        daño += daño_recurso
        print("🚨 SIN ENERGÍA")

    if daño > 0:
        vida -= daño
        print(f"💔 El grupo pierde {daño} salud")


# LOOP PRINCIPAL
for dia in range(1, dias+1):

    mostrar_estado(dia)

    consumo_diario()

    evento_random()

    verificar_recursos()

    if vida <= 0:
        print("\n☠️====================================☠️")
        print("             GAME OVER")
        print("      El grupo no sobrevivió")
        print("☠️====================================☠️")
        break

    if dia == dias:
        print("\n🏆====================================🏆")
        print("        ¡SOBREVIVIERON 10 DÍAS!")
        print("🏆====================================🏆")