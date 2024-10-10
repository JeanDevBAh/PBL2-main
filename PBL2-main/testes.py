import time
import random
import keyboard
import os

def criarmatriz(linhas, colunas):
    matriz = []
    for l in range(linhas):
        linha = []
        for c in range(colunas):
            linha.append('⬛')
        matriz.append(linha)
    return matriz

def printmatriz(matriz):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the terminal
    for l in matriz:
        for e in l:
            print(f'{e}', end= '')
        print()

def inserirpeca(matriz, peca, x, y):
    for i in range(len(peca)):
        for j in range(len(peca[i])):
            if peca[i][j] != '⬛':
                matriz[x + i][y + j] = peca[i][j]

def limparpeca(matriz, peca, x, y):
    for i in range(len(peca)):
        for j in range(len(peca[i])):
            if peca[i][j] != '⬛':
                matriz[x + i][y + j] = '⬛'

def colisao(matriz, peca, x, y):
    for i in range(len(peca)):
        for j in range(len(peca[i])):
            if peca[i][j] != '⬛':  # Consider only filled parts of the piece
                if (x + i >= len(matriz)) or (y + j >= len(matriz[0])) or (y + j < 0):  # Out of bounds
                    return True
                if matriz[x + i][y + j] != '⬛':  # Collision with another piece
                    return True
    return False

def mover_baixo(matriz, peca, x, y):
    limparpeca(matriz, peca, x, y)
    if not colisao(matriz, peca, x + 1, y):  # Check if moving down is possible
        x += 1  # Move down
    inserirpeca(matriz, peca, x, y)
    return x

def mover_esquerda(matriz, peca, x, y):
    limparpeca(matriz, peca, x, y)
    if not colisao(matriz, peca, x, y - 1):  # Move left if no collision
        y -= 1
    inserirpeca(matriz, peca, x, y)
    return y

def mover_direita(matriz, peca, x, y):
    limparpeca(matriz, peca, x, y)
    if not colisao(matriz, peca, x, y + 1):  # Move right if no collision
        y += 1
    inserirpeca(matriz, peca, x, y)
    return y

def gerar_nova_peca():
    return random.choice(peças)

# Tetris pieces
peças = [
    [['🟩', '🟩', '🟩', '🟩']],  # I
    [['🟩', '🟩'], ['🟩', '🟩']],  # O
    [['🟩','🟩', '🟩'], ['⬛', '🟩', '⬛']],  # T
    [['🟩', '🟩', '⬛'], ['⬛', '🟩', '🟩']],  # S
    [['⬛', '🟩','🟩'], ['🟩', '🟩', '⬛']],  # Z
    [['⬛', '⬛', '🟩'], ['🟩', '🟩', '🟩']],  # L
    [['🟩', '⬛', '⬛'], ['🟩', '🟩', '🟩']]   # J
]

# Initialize the game
matriz = criarmatriz(20, 10)
peca = gerar_nova_peca()
x, y = 0, 3  # Starting position

# Game loop
while True:
    time.sleep(0.1)  # Gravity, piece moves down every 0.5 seconds
    limparpeca(matriz, peca, x, y)  # Clear the current piece from the board

    # Handle user input
    if keyboard.is_pressed('left'):
        y = mover_esquerda(matriz, peca, x, y)
    elif keyboard.is_pressed('right'):
        y = mover_direita(matriz, peca, x, y)

    # Move piece down
    if not colisao(matriz, peca, x + 1, y):
        x = mover_baixo(matriz, peca, x, y)
    else:
        # Lock piece in place and generate a new piece
        inserirpeca(matriz, peca, x, y)
        peca = gerar_nova_peca()
        x, y = 0, 3  # Reset to the top
        if colisao(matriz, peca, x, y):  # Game over condition
            print("Game Over!")
            break

    inserirpeca(matriz, peca, x, y)  # Place the piece in its new position
    printmatriz(matriz)  # Update the board

print("Thanks for playing!")
