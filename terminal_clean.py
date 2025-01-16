import os
import time

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def limpiar_terminal_1s():
    # Esperar 10 segundos para que se vean los mensajes
    time.sleep(1.5)
    # Limpiar la terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def limpiar_terminal_2s():
    # Esperar 10 segundos para que se vean los mensajes
    time.sleep(2.5)
    # Limpiar la terminal
    os.system('cls' if os.name == 'nt' else 'clear')