from random import randint
import random

options = ["Piedra", "Papel", "Tijeras"]


# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    resultado = ""
    player = player.lower()
    ai = ai.lower()
    if player == options[0].lower():
        if ai == options[0].lower():
            resultado = "Empate!"
        elif ai == options[1].lower():
            resultado = "Perdiste!"
        elif ai == options[2].lower():
            resultado = "Ganaste!"
    elif player == options[1].lower():
        if ai == options[0].lower():
            resultado = "Ganaste!"
        elif ai == options[1].lower():
            resultado = "Empate!"
        elif ai == options[2].lower():
            resultado = "Perdiste!"
    elif player == options[2].lower():
        if ai == options[0].lower():
            resultado = "Perdiste!"
        elif ai == options[1].lower():
            resultado = "Ganaste!"
        elif ai == options[2].lower():
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
