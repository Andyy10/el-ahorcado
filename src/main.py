# librerías necesarias para que el juego funcione
import random
from arte_ahorcado import logo, ahorcado
from palabras_ahorcado import lista_palabras

# vidas dadas al usuario. por defecto se asignan seis (6)
vidas = 6

print(logo)

palabra_elegida = random.choice(lista_palabras)
#print(palabra_elegida)

# placeholder para mostrar al usuario la longitud de la palabra a adivinar
placeholder = ''
longitud_palabra = len(palabra_elegida)
placeholder += '_ ' * longitud_palabra
print(f'Palabra a adivinar: {placeholder}')

# boolean que determina si el jugador ha perdido o ha ganado
game_over = False
# array para almacenar las letras adivinadas
letras_adivinadas = []

while not game_over:
    print(f'------------------------------- ¡TE QUEDAN {vidas} / 6 VIDAS! -------------------------------')
    conjetura = input('Adivina una letra: ').lower()


    if conjetura in letras_adivinadas:
        print(f'Ya habías adivinado {conjetura} >:/')

    # muestra las letras adivinadas y no adivinadas
    display = ''

    # llena 'display'
    for letra in palabra_elegida:
        if letra == conjetura:
            display += letra
            letras_adivinadas.append(conjetura)
        elif letra in letras_adivinadas:
            display += letra
        else:
            display += '_ '
        
    print(f'Palabra a adivinar: {display}')

    # si no acierta una letra, se quita una vida
    if conjetura not in palabra_elegida:
        vidas -= 1
        print(f'Te equivocaste, {conjetura} no pertenece a la palabra. Pierdes una vida :(.')
        # si las vidas llegan a cero (0), el juego termina e imprime un mensaje
        if vidas == 0:
            game_over = True
            print(f'------------------------------ LA PALABRA ERA {palabra_elegida}. HAS PERDIDO D:. ------------------------------')
            
    # condición que se debe de cumplir para que el usuario gane, en este caso que no hayan '_' en display
    if '_' not in display:
        game_over = True
        print('------------------------------ ¡GANASTE! :D ------------------------------')
    # imprime el arte ascii del ahorcado
    print(ahorcado[vidas])
