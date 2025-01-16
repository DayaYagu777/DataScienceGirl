def font_styling():
    global verde, rojo, negrilla, reset
    verde = "\033[92m"
    rojo = "\033[91m"
    negrilla = "\033[1m"
    reset = "\033[0m"

# Llama a la función para inicializar los estilos
font_styling()