# El Juego del Ahorcado 
(Fecha de actualización: 23 ago 2025)
## Descripción
Este es un proyecto simple del clásico juego del Ahorcado, desarrollado en Python. El objetivo principal es que el usuario pueda adivinar una palabra secreta, letra por letra, antes de quedarse sin intentos. El juego ofrece diferentes niveles de dificultad, lo que lo hace ideal para cualquier tipo de jugador.

## Objetivo del Programa
El propósito de este programa es doble:
1.	**Educativo**: Servir como una herramienta de aprendizaje para principiantes en Python, demostrando conceptos fundamentales como bucles while y for, estructuras condicionales if-elif-else, el uso de funciones y estructuras de datos como listas y sets.
2.	**Entretenimiento**: Proporcionar una experiencia de juego sencilla y divertida, con la posibilidad de elegir la dificultad y jugar múltiples partidas.

## Funcionalidades Principales
El juego del Ahorcado cuenta con las siguientes funcionalidades clave:
- **Selección de Dificultad**: El usuario puede elegir entre tres niveles de dificultad (fácil, medio, difícil), cada uno con su propia lista de palabras secretas.
- **Adivinanza de Letras**: El jugador puede ingresar una letra en cada turno para intentar adivinar la palabra. El programa valida que la entrada sea una sola letra válida.
- **Conteo de Intentos**: El juego tiene un límite de 6 intentos. Por cada letra incorrecta, el contador de intentos disminuye.
- **Visualización del Progreso**: Muestra la palabra con las letras adivinadas y los espacios en blanco (_), lo que permite al jugador ver su progreso.
- **Lógica de Juego**: Maneja las condiciones de victoria y derrota, y notifica al jugador si ha ganado o perdido.
- **Reinicio de Partida**: Ofrece la opción de jugar de nuevo al final de cada partida, sin necesidad de reiniciar el programa.

## Explicación del Código 
A continuación, se explican en detalle algunas líneas y conceptos clave del código, basándose en la sintaxis y la lógica de Python.

## 1. Estructuras de Datos
En el código, se utilizan varias estructuras de datos, cada una con un propósito específico:
- **Listas ([])**: Para las listas de palabras (palabras_facil, palabras_medio, palabras_dificil), se usan corchetes [] para crear una colección ordenada y modificable de elementos. Esto permite que el programa elija un elemento de la lista usando random.choice().
- **Conjuntos (set())**: La variable letras_adivinadas = set() crea un conjunto vacío. Los conjuntos se usan porque garantizan que cada elemento sea único y permiten verificar de forma muy eficiente si una letra ya ha sido adivinada (letra_jugador in letras_adivinadas).

## 2. Control de Flujo: Bucles y Decisiones
El código se basa en bucles para repetir acciones y en estructuras condicionales para tomar decisiones.
- **while True:**: Este bucle while se usa para el menú de dificultad. La condición True hace que el bucle se repita indefinidamente hasta que se encuentre una instrucción break, que en este caso solo ocurre cuando el usuario elige una opción de dificultad válida ('f', 'm', 'd').
- **if-elif-else**: Esta estructura de control se usa para tomar decisiones encadenadas.
  - **if**: Es la primera condición que se evalúa ("Si la elección es 'f'").
  - **elif**: Se evalúa solo si la condición anterior fue falsa ("Sino, si la elección es 'm'"). Puedes tener múltiples elif.
  - **else**: Es la opción por defecto que se ejecuta solo si todas las condiciones anteriores fueron falsas ("Sino, si no fue ninguna de las opciones anteriores").
- **for**: El bucle for letra in palabra_secreta se usa para iterar sobre cada letra de la palabra secreta. Por cada letra, el código dentro del bucle se ejecuta una vez, permitiendo construir la palabra_oculta que se muestra al jugador.

## 3. Operadores y Métodos
El código utiliza operadores y métodos que son fundamentales para la lógica del juego:
- **input().lower()**: La función input() lee la entrada del usuario. El método .lower() convierte la cadena de texto a minúsculas, asegurando que las entradas del usuario como 'F' o 'f' sean tratadas de la misma manera.
- **len() y .isalpha()**: La línea if len(letra_jugador) != 1 or not letra_jugador.isalpha(): es una validación de entrada.
  - len(letra_jugador) != 1: Comprueba si la longitud de la entrada es diferente de 1.
  - not letra_jugador.isalpha(): Verifica si la entrada no es una letra del alfabeto. El or combina ambas condiciones, lo que significa que la entrada es inválida si no es una sola letra.
- **+= y -=**: Estos son operadores de asignación compuesta. Simplifican el código:
  - palabra_oculta += letra + " ": Es una abreviatura de palabra_oculta = palabra_oculta + (letra + " ").
  - intentos_restantes -= 1: Es una abreviatura de intentos_restantes = intentos_restantes - 1.
- **f"" (f-strings)**: El prefijo f antes de una cadena, como en print(f"\nPalabra: {palabra_oculta}"), se usa para incrustar variables directamente en la cadena de texto de manera limpia y legible.

## Instrucciones para juagar
Seguir los pasos que aparecen en la terminal.
