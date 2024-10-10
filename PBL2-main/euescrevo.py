import time
import os
import random
import keyboard

def criarmatriz(linhas, colunas): #certo
    matriz = []
    for l in range(linhas):
        linha = []
        for c in range(colunas):
            linha.append('⬛')
        matriz.append(linha)
    return matriz

def printmatriz(matriz):
    os.system('cls')
    for l in matriz:
        for e in l:
            print(f'{e}', end= '')
        print()

def inserirpeca(matriz, peca, x, y):
    for i in range(len(peca)):
        for j in range(len(peca[i])):
            if peca[i][j] != '⬛':  
                matriz[x + i][y + j] = peca[i][j]


def Pode_mover(matriz, peca, x, y):
      for i in range(len(peca)):
        for j in range(len(peca[i])):
            if peca[i][j] != '⬛':  
                if (x + i >= len(matriz)) or (y + j >= len(matriz[0])) or (y + j < 0): 
                    return True
                if matriz[x + i][y + j] != '⬛':  
                    return True
      return False

def mover_baixo(matriz, peca, x, y):
      limparpeca(matriz, peca, x, y)
      if not Pode_mover(matriz, peca, x + 1, y):  
        x += 1  
      inserirpeca(matriz, peca, x, y)
      return x  

def remove_linha(matriz):
    pontos = 0
    contapontos = 0
    for i, linha in enumerate(matriz):
        if linha.count('🟩') == len(linha) and not Pode_mover(matriz, peca, x, y):
            contapontos += 1
            matriz.pop(i)  
            matriz.insert(0, ['⬛' for e in range(10)])    
    if contapontos == 1:
        pontos += 100
    elif contapontos > 1:
        pontos += (100 * contapontos) * 2
    return pontos


def mover_direita(matriz, peca, x, y):
      limparpeca(matriz, peca, x, y)
      if not Pode_mover(matriz, peca, x , y + 1):  
        y += 1  
      return y  

def mover_esquerda(matriz, peca, x, y):
      limparpeca(matriz, peca, x, y)
      if not Pode_mover(matriz, peca, x, y - 1): 
        y -= 1  
      return y  

def rotacionar_peca(peca):
    
    return [list(reversed(y)) for y in zip(*peca)]

def rotacionar_e_inserir(matriz, peca, x, y):
    nova_peca = rotacionar_peca(peca)
    limparpeca(matriz, peca, x, y)  
    if not Pode_mover(matriz, nova_peca, x, y):  
        peca = nova_peca  
    return peca 

def tempojg(s):
    time.sleep(s)
    

def limparpeca(matriz, peca, x, y):
     for i in range(len(peca)):
        for j in range(len(peca[i])):
            if peca[i][j] != '⬛':  
                matriz[x + i][y + j] = '⬛'

def gerar_nova_peca():
    return random.choice(peças)

peças = [
    
    [['🟩', '🟩', '🟩', '🟩']], # I
    #[['🟩', '🟩'], ['🟩', '🟩']], # O
    #[['🟩','🟩', '🟩'], ['⬛', '🟩', '⬛']], # T
    #[['🟩', '🟩', '⬛'], ['⬛', '🟩', '🟩']], # S
    #[['⬛', '🟩','🟩'], ['🟩', '🟩', '⬛']], # Z
    #[['⬛', '⬛', '🟩'], ['🟩', '🟩', '🟩']], # L
    #[['🟩', '⬛', '⬛'], ['🟩', '🟩', '🟩']],  # J
    #[['⬛','⬛','⬛'], ['⬛','💣','⬛'],['⬛','⬛','⬛']]
]


matriz = criarmatriz(20, 10)
peca = gerar_nova_peca()
x, y = 0, random.randint(2,6)  
verifica = True
pontuação = 0

while verifica == True:
    print(f'{'-='*40}'
        '\nCONTROLES: w(girar), s(acelerar), a(esquerda), d(direita)')
    print( 
           f'{'-='*40}'
           f'\nPONTOS: {pontuação}'
           )
    if keyboard.is_pressed('s'):
        tempojg(0.1)
    else:
        tempojg(0.5)
    
    limparpeca(matriz, peca, x, y)
    if keyboard.is_pressed('a'):
        y = mover_esquerda(matriz, peca, x, y)
    if keyboard.is_pressed('d'):
        y = mover_direita(matriz, peca, x, y)
    if keyboard.is_pressed('w'):  
        peca = rotacionar_e_inserir(matriz, peca, x, y)
    
    if not Pode_mover(matriz, peca, x + 1, y):
         x = mover_baixo(matriz, peca, x, y)

    else:
        
        inserirpeca(matriz, peca, x, y)
        peca = gerar_nova_peca()
        x, y = 0, random.randint(2,6) 
        pontuação += remove_linha(matriz) 
        remove_linha(matriz)
        
        if Pode_mover(matriz, peca, x, y):  
            print("Game Over!")
            verifica = False

    
    inserirpeca(matriz, peca, x, y)
    printmatriz(matriz) 
    
   
print("Game Over!")