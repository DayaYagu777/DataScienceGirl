import random
import getpass
from terminal_clean import limpiar_terminal_1s, limpiar_terminal_2s, limpiar_terminal
from game_results import *
from user_menu import *
from font_styling import *

# Variables globales para la dificultad y puntajes
global dificultad, puntaje_gana, puntaje_pierde

def mostrar_bienvenida(nombre):
    """Muestra un mensaje de bienvenida al jugador."""
    print(f"\n{rojo}BIENVENIDO, {nombre}!{reset}")
    print("\nADIVINA EL NÚMERO")
    print("-----------------------------")

# Función para el submenú de dificultad
def submenu():
    """Muestra las opciones de dificultad y permite al usuario seleccionar una."""
    global dificultad
    ancho = 20  # Ancho del marco para imprimir las opciones

    # Imprimir el marco superior
    print("+" + "-" * (ancho - 2) + "+")
    print("|" + "NIVELES DE DIFICULTAD".center(ancho - 2) + "|")
    print("+" + "-" * (ancho - 2) + "+")

    # Opciones de dificultad
    niveles = [
        "1. Fácil",
        "2. Medio",
        "3. Difícil"
    ]

    # Imprimir las opciones
    for nivel in niveles:
        print("| " + nivel.ljust(ancho - 2) + " |")

    # Imprimir el marco inferior
    print("+" + "-" * (ancho - 2) + "+")

    # Solicitar al usuario que elija una opción
    while True:
        try:
            dificultad = int(input("\nElige la opción (1,2,3) ---> "))
            if 1 <= dificultad <= 3:
                return dificultad  # Retornar la dificultad elegida
            else:
                print(f"\n{rojo}Opción inválida. Por favor, elige una opción entre 1 y 3.{reset}")
        except ValueError:
            print(f"\n{rojo}Entrada no válida. Por favor, introduce un número.{reset}")

def establecer_intentos(dificultad):
    """Establece el número de intentos y puntajes según la dificultad seleccionada."""
    global puntaje_gana, puntaje_pierde

    # Definir intentos y puntajes según la dificultad
    if dificultad == 1:
        puntaje_gana = 2
        puntaje_pierde = 0
        return 20  # Retornar intentos para dificultad fácil
    elif dificultad == 2:
        puntaje_gana = 5
        puntaje_pierde = 0
        return 12  # Retornar intentos para dificultad media
    elif dificultad == 3:
        puntaje_gana = 10
        puntaje_pierde = 0
        return 5   # Retornar intentos para dificultad difícil
    else:
        print(f"{rojo}Dificultad no válida.{reset}")
        return 0

def grafico_ganar(puntaje):
    """Muestra un gráfico de barras simple cuando el jugador gana."""
    print(f"\n{verde}¡Has ganado! En esta partida:{reset}")
    print("Puntos: " + str(puntaje) + "pt")
    print(f"{rojo}" + "█" * puntaje + f"{reset}")  # Gráfico de barras simple
    limpiar_terminal_2s()

def grafico_perder(intentos, puntaje):
    """Muestra un gráfico de barras simple cuando el jugador pierde."""
    print(f"\n{rojo}¡Has perdido! En esta partida:{reset}")
    print("Intentos agotados: " + str(intentos) + "\nPuntos: " + str(puntaje) + "pt")
    print(f"{rojo}" + "░" * puntaje + f"{reset}")  # Gráfico de barras simple
    limpiar_terminal_2s()

# Función para jugar a adivinar el número (modo solitario)
def modo_solitario(intentos, nombre):
    """Implementa el modo solitario del juego, donde el jugador intenta adivinar un número."""
    global puntaje
    num_gener = random.randint(1, 1000)  # Generar un número aleatorio entre 1 y 1000
    limpiar_terminal()
    print("\nHa iniciado el juego! Tienes {} intentos.\n".format(intentos))

    for intento in range(intentos):
        try:
            num_user = int(input("\nIngresa un número entre 1 y 1000: "))
            if 1 <= num_user <= 1000:
                if num_user == num_gener:
                    puntaje = puntaje_gana
                    grafico_ganar(puntaje)
                    guardar_resultados(nombre, 'Modo solitario', dificultad, 'Ganó', int(puntaje))
                    return
                elif num_user > num_gener:
                    print("\nInténtalo otra vez, ¿Qué número tengo?")
                    print(f"Te quedan {intentos - (intento + 1)} intentos.")
                    print(f'{verde}No es correcto. El número es menor a {num_user}{reset}')
                    limpiar_terminal_1s()
                else:
                    print("\nInténtalo otra vez, ¿Qué número tengo?")
                    print(f"Te quedan {intentos - (intento + 1)} intentos.")
                    print(f'{verde}No es correcto. El número es mayor a {num_user}{reset}')
                    limpiar_terminal_1s()
            else:
                print(f"\n{rojo}El número debe estar entre 1 y 1000.{reset}")
        except ValueError:
            print(f"\n{rojo}Entrada no válida. Por favor, introduce un número.{reset}")

    # Si se agotan los intentos
    puntaje = puntaje_pierde
    grafico_perder(intentos, puntaje)
    guardar_resultados(nombre, 'Modo solitario', dificultad, 'Perdió', int(puntaje))


# Función para jugar a adivinar el número (modo dos jugadores)
def modo_partida_dos_jugadores(intentos,nombre):
    """Implementa el modo partida dos jugadores, donde el jugador intenta adivinar un número."""
    global puntaje
    num_user1 = int(getpass.getpass("Usuario 1: Ingresa un número entre 1 y 1000: "))

    limpiar_terminal()  # Limpiar la terminal después de que el usuario 1 ingresa el número

    for intento in range(intentos):
        try:
            num_user2 = int(input("Usuario 2: Ingresa un número entre 1 y 1000: "))
            if 1 <= num_user2 <= 1000:
                if num_user1 == num_user2:
                    puntaje = puntaje_gana
                    grafico_ganar(puntaje)
                    guardar_resultados(nombre, 'Modo dos jugadores', dificultad, 'Ganó', int(puntaje))
                    return
                elif num_user1 > num_user2:
                    print("\nInténtalo otra vez, ¿Qué número tengo?")
                    print(f"Te quedan {intentos - (intento + 1)} intentos.")
                    print(f'{verde}No es correcto. El número es mayor a {num_user2}{reset}')
                    limpiar_terminal_1s()
                else:
                    print("\nInténtalo otra vez, ¿Qué número tengo?")
                    print(f"Te quedan {intentos - (intento + 1)} intentos.")
                    print(f'{verde}No es correcto. El número es menor a {num_user2}{reset}')
                    limpiar_terminal_1s()
            else:
                print(f"\n{rojo}El número debe estar entre 1 y 1000.{reset}")
        except ValueError:
            print(f"\n{rojo}Entrada no válida. Por favor, introduce un número.{reset}")

    puntaje = puntaje_pierde
    grafico_perder(intentos, puntaje)
    guardar_resultados(nombre, 'Modo dos jugadores', dificultad, 'Perdió', int(puntaje))