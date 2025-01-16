'''
--------- Módulo Principal Main ---------------------

URL: https://github.com/DayaYagu777/DataScienceGirl
Descripción: Este módulo contiene la lógica principal del juego de adivinanza de números.

IMPORTANTE: Ejecutar en Visual Studio Code
'''

# Importa librerías
import os  # Importar os para manejar rutas de archivos

# Importar módulos del usuario
from terminal_clean import limpiar_terminal, limpiar_terminal_2s
from font_styling import *
from user_menu import menu
from game_logic import *
from game_logic import mostrar_bienvenida, modo_solitario, modo_partida_dos_jugadores 
from game_results import mostrar_estadistica

def main():
    '''
    Contiene la estructura principal del juego.
    Une en secuencia y de forma sistemática los módulos para navegar y arrancar el juego.
    Variables globales:
        nombre (str): Nombre del jugador.
        intentos (int): Número de intentos permitidos.
        ruta_archivo (str): Ruta del archivo donde se guardarán los resultados del juego.
    '''
    global nombre, intentos, ruta_archivo  

    # Borrar cualquier archivo anterior
    if os.path.exists(ruta_archivo):
        os.remove(ruta_archivo)

    # Ruta del archivo donde se guardarán los resultados del juego
    ruta_archivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resultados_juego.xlsx')

    # Mensaje de bienvenida personalizado
    print(f"\n{rojo}BIENVENIDO!{reset}")
    print("\nADIVINA EL NÚMERO")
    print("-----------------------------")
    
    # Solicitar el nombre del jugador
    nombre = input(f"{rojo}Para comenzar, por favor ingresa tu nombre:\n{reset}")
    mostrar_bienvenida(nombre) 

    limpiar_terminal()  

    # Bucle principal del juego
    while True:
        opcion_menu = menu()  # Llamar a la función menú para mostrar opciones
        if opcion_menu == 1:  # Modo de juego: partida modo solitario
            limpiar_terminal() 
            dificultad = submenu()  # Seleccionar dificultad
            intentos = establecer_intentos(dificultad)  # Establecer intentos según dificultad
            modo_solitario(intentos, nombre)  

        elif opcion_menu == 2:  # Modo de juego: partida para 2 jugadores
            limpiar_terminal()
            dificultad = submenu()  
            intentos = establecer_intentos(dificultad)  
            modo_partida_dos_jugadores(intentos, nombre)  

        elif opcion_menu == 3:  # Opción para mostrar estadísticas
            mostrar_estadistica(nombre)  

        elif opcion_menu == 4:  # Opción para salir del juego
            limpiar_terminal_2s()
            print(f"\n{rojo} ¡Hasta luego! {nombre}{reset}") 

            # Eliminar archivo de resultados si existe
            if os.path.exists(ruta_archivo):
                os.remove(ruta_archivo)
            else:
                print("No has jugado aún. No tenemos un archivo de resultados.")
            break

# Llamar a la función principal
main()
