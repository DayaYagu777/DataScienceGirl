import os
import time

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def limpiar_terminal_1s():
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')

def limpiar_terminal_2s():
    time.sleep(2.5)
    os.system('cls' if os.name == 'nt' else 'clear')
