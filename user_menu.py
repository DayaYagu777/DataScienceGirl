from font_styling import *  # Importar estilos para formatear la salida en consola

# Función para mostrar el menú principal del juego
def menu():
    # Mostrar el título del menú en negrita
    print(f"\n{negrilla}MENÚ{reset}")
    
    # Lista de opciones disponibles en el menú
    opciones = [
        "1. Partida modo solitario",  # Opción para jugar solo
        "2. Partida 2 Jugadores",      # Opción para jugar en modo multijugador
        "3. Estadística",              # Opción para ver estadísticas del jugador
        "4. Salir"                     # Opción para salir del juego
    ]

    # Imprimir cada opción del menú
    for opcion in opciones:
        print(opcion)

    # Bucle para solicitar una opción válida al usuario
    while True:
        try:
            # Solicitar al usuario que elija una opción
            opcion_menu = int(input("\nElige la opción (1,2,3,4) ---> "))
            # Verificar que la opción esté dentro del rango válido
            if 1 <= opcion_menu <= 4:
                return opcion_menu  # Retornar la opción seleccionada
            else:
                # Mensaje de error si la opción está fuera del rango
                print(f"\n{rojo}Opción inválida. Por favor, elige una opción entre 1 y 4.{reset}")
        except ValueError:
            # Mensaje de error si la entrada no es un número
            print(f"\n{rojo}Entrada no válida. Por favor, introduce un número.{reset}")