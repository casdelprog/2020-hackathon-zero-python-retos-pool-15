from random import randint
import random

options = ["Piedra", "Papel", "Tijeras"]


# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player = player.lower()
    ai = ai.lower()
    resultado = ""
    if player == options[0]:
        if ai == options[0]:
            resultado = "Empate!"
        elif ai == options[1]:
            resultado = "Perdiste!"
        elif ai == options[2]:
            resultado = "Ganaste!"
    elif player == options[1]:
        if ai == options[0]:
            resultado = "Ganaste!"
        elif ai == options[1]:
            resultado = "Empate!"
        elif ai == options[2]:
            resultado = "Perdiste!"
    elif player == options[2]:
        if ai == options[0]:
            resultado = "Perdiste!"
        elif ai == options[1]:
            resultado = "Ganaste!"
        elif ai == options[2]:
            resultado = "Empate!"
    return resultado

# Entry Point
def Game():
    #
    #
    
    #
    #
    player = input("Escribe: Piedra, Papel o Tijeras")
    ai = options[random.choice(range(3))]
    winner = quienGana(player, ai)

    print(winner)

