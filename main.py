import os  # Importar os para manejar rutas de archivos
from terminal_clean import limpiar_terminal,limpiar_terminal_2s
from font_styling import *
from user_menu import menu
from game_logic import *
from game_logic import mostrar_bienvenida, modo_solitario, modo_partida_dos_jugadores 
from game_results import mostrar_estadistica


# Lógica principal del juego
def main():
    global nombre, intentos, ruta_archivo  # Definir variables globales
    # Definir la ruta del archivo donde se guardarán los resultados del juego
    ruta_archivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resultados_juego.xlsx')

    # Mensaje de bienvenida
    print(f"\n{rojo}BIENVENIDO!{reset}")
    print("\nADIVINA EL NÚMERO")
    print("-----------------------------")
    
    # Solicitar el nombre del jugador
    nombre = input("Para comenzar, por favor ingresa tu nombre:\n")
    mostrar_bienvenida(nombre)  # Mostrar mensaje de bienvenida personalizado

    limpiar_terminal()  # Limpiar la terminal para un mejor inicio

    # Bucle principal del juego
    while True:
        opcion_menu = menu()  # Llamar a la función menú para mostrar opciones
        if opcion_menu == 1:  # Modo de juego: partida modo solitario
            limpiar_terminal()  # Limpiar la terminal
            dificultad = submenu()  # Llamar a la función submenu para seleccionar dificultad
            intentos = establecer_intentos(dificultad)  # Establecer el número de intentos según la dificultad
            modo_solitario(intentos, nombre)  # Iniciar el juego en modo solitario

        elif opcion_menu == 2:  # Modo de juego: partida para 2 jugadores
            limpiar_terminal()  # Limpiar la terminal
            dificultad = submenu()  # Llamar a la función submenu para seleccionar dificultad
            intentos = establecer_intentos(dificultad)  # Establecer el número de intentos según la dificultad
            modo_partida_dos_jugadores(intentos, nombre)  # Iniciar el juego en modo de 2 jugadores

        elif opcion_menu == 3:  # Opción para mostrar estadísticas
            mostrar_estadistica(nombre)  # Mostrar las estadísticas del jugador

        elif opcion_menu == 4:  # Opción para salir del juego
            limpiar_terminal_2s()
            print(f"\n{rojo} ¡Hasta luego! {nombre}{reset}")  # Mensaje de despedida

            if os.path.exists(ruta_archivo):
                os.remove(ruta_archivo)
            else:
                print("No has jugado aún. No tenemos un archivo de resultados.")
            break

# Llamar a la función principal para iniciar el juego
main()