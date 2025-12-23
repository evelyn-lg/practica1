'''
Docstring for curso w3.basic_projects.guessnumber
2. Adivina el número
Descripción: La computadora elige un número aleatorio entre 1 y 100,
y el usuario debe adivinarlo con pistas ("mayor" o "menor").

Conceptos: random.randint(), bucles while, comparaciones.

Extra: Llevar un conteo de intentos y ofrecer jugar de nuevo.
'''
import random

num = random.randint(1, 100)

u = input("Adivina un número entre 1 y 100: ")
attempts = 0

while True:
    attempts += 1
    try:
        guess = int(u)
    except ValueError:
        u = input("Por favor, ingresa un número válido: ")
        continue

    if guess < num:
        u = input("El número es mayor. Intenta de nuevo: ")
    elif guess > num:
        u = input("El número es menor. Intenta de nuevo: ")
    else:
        print(f"¡Felicidades! Adivinaste el número {num} en {attempts} intentos.")
        play_again = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if play_again == 's':
            num = random.randint(1, 100)
            attempts = 0
            u = input("Adivina un número entre 1 y 100: ")
        else:
            print("Gracias por jugar. ¡Hasta luego!")
            break