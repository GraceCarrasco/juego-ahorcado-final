print ("¡Bienvenido al juego del Ahorcado!")
print ("Trata de adivinar la palabra secreta. Tienes 6 intentos")

import random # Importa el modulo para elegir palabras al azar

palabras_facil = ["casa", "perro", "gato", "sol"]
palabras_medio = ["computadora", "universidad", "programacion"]
palabras_dificil = ["paralelepipedo", "otorrinolaringologo"]

# Aqui ira el codigo para que el jugador elija la dificultad
# Por ahora para el avance, se va a elegir una dificultad fija
palabra_secreta = random.choice(palabras_facil)

letras_adivinadas = []
letras_falladas = []
intentos_restantes = 6

# Este es el bucle principal que se repite hasta que el juego termina
while intentos_restantes > 0:
    # Aqui ira la logica principal del juego
    pass  # 'pass' es un marcador de posición, se cambiara despues

# Este código se ejecuta cuando el bucle termina (después de ganar o perder)
print("¡Fin del juego!")