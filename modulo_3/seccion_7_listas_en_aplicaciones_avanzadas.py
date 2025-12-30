
board = []

for i in range(8):
    row = ['EMPTY' for i in range(8)]
    board.append(row)

print(board)

board[0][0] = 'ROOK'
board[0][7] = 'ROOK'
board[7][0] = 'ROOK'
board[7][7] = 'ROOK'

print(board)

board[4][2] = 'KNIGHT'

print(board)

# Crear un hotel de 3 edificios con 15 pisos cada edificio y 20 habitaaciones por planta

hotel = [[[False for r in range(20)]for f in range(15)]for t in range (3)]

# Asignar una habitacion a una pareja en el segundo edificio, decimo piso, habitacion nº 14

hotel[1][9][13] = True

# Asignar 3 habitaciones del edificio 3 en el piso 15

hotel[2][14][15] = True
hotel[2][14][3] = True

# Verificar si hay disponibilidad en el piso 15 del tercer edificio

vacancy = 0

for room_number in range(20):
    if not hotel[2][14][room_number]:
        vacancy += 1

print(vacancy)



