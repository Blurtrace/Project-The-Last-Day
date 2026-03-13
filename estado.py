dias_sin_agua=0 
agua=100
salud=100
ernergia=100
comida=100
import random
def calcular_dias_restantes(dia_actual, meta_dias=10):
    """Calcula cuántos días faltan para terminar."""
    return meta_dias - dia_actual

def predecir_muerte_por_sed(dias_sin_agua, dias_restantes):
    """Predice si el límite de 3 días sin agua ocurrirá antes del día 10."""
    # Si sumamos los días que ya lleva sin agua + los que faltan, y da 3 o más
    return (dias_sin_agua + dias_restantes) >= 3

def predecir_muerte_por_hambre(salud_actual, daño_diario, dias_restantes):
    """Predice si la salud llegará a 0 antes del día 10 por falta de comida."""
    daño_total_esperado = daño_diario * dias_restantes
    return salud_actual <= daño_total_esperado

def ejecutar_verificacion_derrota(salud, agua, comida, dias_sin_agua, dia_actual):
    """Coordina las predicciones y decide si el juego termina."""
    faltan = calcular_dias_restantes(dia_actual)
    

def calcular_daño_restante(daño_diario, dias_que_faltan):
    """Calcula cuánto daño total recibirá el jugador hasta el día 10."""
    return daño_diario * dias_que_faltan

def verificar_viabilidad_salud(salud_actual, daño_total_futuro):
    """Compara si la salud actual es suficiente para soportar el daño futuro."""
    # Si la salud es menor o igual al daño que viene, el destino es la derrota
    return salud_actual > daño_total_futuro

def emitir_alerta_derrota(salud, dias_restantes):
    """Muestra el mensaje de que la salud no alcanzará para terminar."""
    print(f"--- ALERTA DE PREVISIÓN ---")
    print(f"Con {salud} de salud no es posible sobrevivir {dias_restantes} días más.")
    print("GAME OVER: Agotamiento inevitable antes del día 10.")
# condicion de muerte por llegar a 0
def esta_muerto(salud):
    """Tarea única: Evaluar si la salud cayó a un nivel crítico (0 o menos)."""
    return salud <= 0

def finalizar_juego(causa):
    """Tarea única: Informar al jugador que el juego terminó y la razón."""
    print("\n-------------------------------------------")
    print(f"GAME OVER: El juego ha finalizado.")
    print(f"Causa de muerte: {causa}.")
    print("-------------------------------------------")

def verificar_estado_vital(salud_actual):
    """Tarea única: Coordinar si el juego debe cerrarse por falta de salud."""
    if esta_muerto(salud_actual):
        finalizar_juego("Salud agotada (Daño acumulado)")
        return True  # Devuelve True para indicar que el juego se detiene
    return False # Devuelve False para indicar que el jugador sigue vivo