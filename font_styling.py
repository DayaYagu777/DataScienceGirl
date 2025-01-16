def font_styling():
    '''
    Cambia el color del texto en la terminal utilizando códigos de escape ANSI.
    
    Variables globales:
        verde (str): Código de escape para el color verde, utilizado para resaltar texto positivo.
        rojo (str): Código de escape para el color rojo, utilizado para resaltar texto de error o advertencia.
        negrilla (str): Código de escape para el texto en negrita, utilizado para enfatizar texto importante.
        reset (str): Código de escape para restablecer el estilo del texto a su valor predeterminado.

    Ejemplo de uso:
        print(f"{verde}Este texto es verde.{reset}")
        
    '''
    global verde, rojo, negrilla, reset
    verde = "\033[92m"
    rojo = "\033[91m"
    negrilla = "\033[1m"
    reset = "\033[0m"

# Arrancar los estilos
font_styling()
