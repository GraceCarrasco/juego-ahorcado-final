print ("¡Bienvenido al juego del Ahorcado!")
print ("Trata de adivinar la palabra secreta. Tienes 6 intentos")

import random # Importa el modulo para elegir palabras al azar

palabras_facil = ["casa", "perro", "gato", "sol"] # Uso de corchetes al ser listas
palabras_medio = ["computadora", "universidad", "programacion"]
palabras_dificil = ["paralelepipedo", "otorrinolaringologo"]

def jugar_ahorcado():
    """Función principal que contiene toda la lógica del juego."""

    # --- Menú para elegir la dificultad ---
    # Esta estructura repetitiva se asegura de que el usuario elija una opción válida.
    while True:
        print("\n--- Elige una dificultad ---")
        print("Fácil (f)")
        print("Medio (m)")
        print("Difícil (d)")
        
        eleccion = input("Ingresa tu elección: ").lower()

        # --- Estructura lógica para seleccionar la lista de palabras ---
        if eleccion == 'f':
            palabra_secreta = random.choice(palabras_facil)
            break
        elif eleccion == 'm':
            palabra_secreta = random.choice(palabras_medio)
            break
        elif eleccion == 'd':
            palabra_secreta = random.choice(palabras_dificil)
            break
        else:
            print("Opción no válida. Por favor, elige 'f', 'm' o 'd'.")

    # --- Configuración inicial del juego ---
    letras_adivinadas = set()
    intentos_restantes = 6

    print("\n¡Iniciando una nueva partida!")
    print("Trata de adivinar la palabra secreta. Tienes 6 intentos.")

    # --- Bucle principal del juego (Estructura repetitiva) ---
    while intentos_restantes > 0:
        palabra_oculta = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_oculta += letra + " "
            else:
                palabra_oculta += "_ "

        print(f"\nPalabra: {palabra_oculta}") # f" significa f-string o cadena formateada
        print(f"Intentos restantes: {intentos_restantes}") 

        if "_ " not in palabra_oculta:
            print("\n¡Felicidades! ¡Has adivinado la palabra!")
            break

        letra_jugador = input("Ingresa una letra: ").lower()

        if len(letra_jugador) != 1 or not letra_jugador.isalpha():  # len() (abreviatura de length) devuelve la longitud o el número de elementos de un objeto y .isalpha() es un método de las cadenas de texto que devuelve un valor booleano (True o False). Su función es verificar si una cadena de texto contiene solo letras del alfabeto. Ignora espacios, números y símbolos.
            print("Entrada inválida. Por favor, ingresa solo una letra.")
        elif letra_jugador in letras_adivinadas:
            print("Ya has intentado esa letra. Intenta con otra.")
        elif letra_jugador in palabra_secreta:
            print("¡Acierto! La letra está en la palabra.")
            letras_adivinadas.add(letra_jugador) # El método .add() es específico de los conjuntos (set). Su única función es agregar un nuevo elemento a un conjunto.
        else:
            print("Error, la letra no está en la palabra.")
            intentos_restantes -= 1
            letras_adivinadas.add(letra_jugador)

    # --- Lógica de fin de juego (Estructura lógica final) ---
    print("\n¡Fin del juego!")
    if intentos_restantes == 0:
        print(f"¡Qué lástima! Te has quedado sin intentos. La palabra secreta era: {palabra_secreta}")
    else:
        print(f"¡Ganaste! La palabra secreta era: {palabra_secreta}")

# --- Bucle para jugar varias veces ---
while True:
    jugar_ahorcado()
    respuesta = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if respuesta != 's':
        break

print("¡Gracias por jugar! ¡Hasta la próxima!")