import os
import time

def limpiar_terminal():
    """
    Limpia la terminal de comandos.
    
    Esta función utiliza el comando adecuado según el sistema operativo:
    'cls' para Windows y 'clear' para sistemas Unix/Linux.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def limpiar_terminal_1s():
    """
    Limpia la terminal después de esperar 1.5 segundos.
    
    Esta función espera 1.5 segundos antes de limpiar la terminal,
    permitiendo que los mensajes sean visibles brevemente antes de ser eliminados.
    """
    time.sleep(1.5)  # Espera 1.5 segundos
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la terminal

def limpiar_terminal_2s():
    """
    Limpia la terminal después de esperar 2.5 segundos.
    
    Esta función espera 2.5 segundos antes de limpiar la terminal,
    permitiendo que los mensajes sean visibles brevemente antes de ser eliminados.
    """
    time.sleep(2.5)  # Espera 2.5 segundos
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la terminal

