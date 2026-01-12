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

from random import randrange
tablero = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
]

# ----------------- FUNCIONES ----------------#

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

# Revisamos si alguien a ganado la partida.
def victory_for(board, sign):
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True
    
    for i in range(3):
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True
        
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    return False


# Movimiento random de la IA
def draw_move(board):
    lista_libre = make_list_of_free_fields(board)

    cantidad = len(lista_libre)

    if cantidad > 0:
        indice_azar = randrange(cantidad)
        row, col = lista_libre[indice_azar]

        board[row][col] = 'X'


#----------- PROGRAMA FINAL ---------------#
# Inicialización: La maquina siempre empieza en el centro (Regla del Juego)
board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]
]


# Bucle del juego
while True:
    display_board(board)

    # ---- Aqui tira el Humano
    enter_move(board)


    if victory_for(board, 'O') == True:
        display_board(board)
        print('You Win!!!')
        break

    if len(make_list_of_free_fields(board)) == 0:
        display_board(board)
        print('Draw')
        break
    
    # ---- Aqui tira la Maquina
    # Mostramos el Tablero para ver el movimiento anterior
    display_board(board)
    draw_move(board)

    if victory_for(board, 'X') == True:
        display_board(board)
        print('You lose')
        break

    if len(make_list_of_free_fields(board)) == 0:
        display_board(board)
        print('Draw')
        break

