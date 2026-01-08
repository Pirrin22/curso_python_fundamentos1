'''
Escenario
Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están nuestras reglas:

- la maquina (por ejemplo, el programa) jugará utilizando las 'X's;
- el usuario (por ejemplo, tu) jugarás utilizando las 'O's;
- el primer movimiento es de la maquina - siempre coloca una 'X' en el centro del tablero;
- todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia)
- el usuario ingresa su movimiento introduciendo el número de cuadro elegido - el número debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado;
- el programa verifica si el juego ha terminado - existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana;
- la maquina responde con su movimiento y se verifica el estado del juego;
- no se debe implementar algún tipo de inteligencia artificial - la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.

'''

import random
tablero = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
]

# Funcion para crear el tablero mas visual.
def display_board(board):
    for fila in board:
        print('+-------+-------+-------+')
        print('|       |       |       |')
        print(f'|   {fila[0]}   |   {fila[1]}   |   {fila[2]}   |')
        print('|       |       |       |')
    print('+-------+-------+-------+')

# Funcion para marcar en el tablero el mvimiento del usuario.
def enter_move(board):
    while True:
        move = int(input('Cual es tu movimiento: '))
        if move < 1 or move > 9:
            print('El numero debe ser entre 1 y 9')
            continue
        for filas in range(3):
            for columna in range(3):
                if board[filas][columna] == move:
                    board[filas][columna] = 'O'
                    return
        print('Esta casilla esta ocupada')

# Funcion para revisar cuadros del tablero sin asignacion.
def make_list_of_free_fields(board):
    libres = []
    for row in range(3):
        for col in range(3):
            if board[row][col] != 'X' and board[row][col] != 'O':
                libres.append((row, col))
    return libres




def victory_for(board, sign):



def draw_move(board):


