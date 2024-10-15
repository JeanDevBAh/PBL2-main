import time #biblioteca time sera usada para simular o movimento do jogo, fazendo o codigo parar por determinado tempo para todos os prints serem mostrados separadamente.
import os #Os sera usada para limpar o terminal.
import random #ramdom sera usada para sortear elementos do jogo.
import keyboard #keyboard sera usada para gerar comandos para o jogo atraves do teclado.

def criarmatriz(linhas, colunas):  #função para criar a matriz que será o tabuleiro do jogo
    matriz = []
    for l in range(linhas): #essa função cria uma lista de listas(matriz) e preenche ela com um emoji de cor preta para simular o fundo.
        linha = []
        for c in range(colunas):
            linha.append('⬛')
        matriz.append(linha)
    return matriz

def printmatriz(matriz): #função para printar a matriz criada anteriormente 
    os.system('cls') #essa função também limpa o terminal sempre que é chamada garantindo que so um tabuleiro seja visivel.
    for l in matriz:
        for e in l:
            print(f'{e}', end= '')
        print()

def inserirpeca(matriz, peca, x, y): #as peças são inseridas nas posições iniciais da matriz substituindo o fundo pelo bloco da peça
    for i in range(len(peca)):
        for j in range(len(peca[i])):
            if peca[i][j] != '⬛':  
                matriz[x + i][y + j] = peca[i][j]


def Pode_mover(matriz, peca, x, y): #verificação da peça dentro do tabuleiro.
      for i in range(len(peca)):
        for j in range(len(peca[i])):
            if peca[i][j] != '⬛':  
                if (x + i >= len(matriz)) or (y + j >= len(matriz[0])) or (y + j < 0): 
                    return True
                if matriz[x + i][y + j] != '⬛':  
                    return True
      return False

def mover_baixo(matriz, peca, x, y): #função para descer a peça
      limparpeca(matriz, peca, x, y) #remove a peça do tabuleiro
      if not Pode_mover(matriz, peca, x + 1, y):  
        x += 1   #se não tiver restriçao no movimento a posiçao das linhas(x) recebe mais 1.
      inserirpeca(matriz, peca, x, y) #insere a peça novamente no tabuleiro.
      return x  #retorna a nova posiçao nas linhas

def remove_linha(matriz): #Funçao para remover as linhas completas e retornar a pontuação obtida pela quantidade de linhas removidas.
    pontos = 0
    contapontos = 0
    for i, linha in enumerate(matriz):
        if linha.count('🟩') == len(linha) and not Pode_mover(matriz, peca, x, y): #verifica se a linha está preenchida após a peça ser inserida.
            contapontos += 1 #conta o numero de linhas removidas
            matriz.pop(i)  #remove a linha
            matriz.insert(0, ['⬛' for e in range(10)]) #insere uma linha nova no topo da matriz
    if contapontos == 1:
        pontos += 100   #pontuaçoes diferentes pelo numero de linhas removidas.
    elif contapontos > 1:
        pontos += (100 * contapontos) * 2
    return pontos #retorna a pontação


def mover_direita(matriz, peca, x, y): #funçao que limpa a peça e verifica se a posiçao da direita está livre. 
      limparpeca(matriz, peca, x, y)
      if not Pode_mover(matriz, peca, x , y + 1):  
        y += 1  #caso ela possa mover a posição das colunas recebe mais 1.
      return y  #retorna a nova posição

def mover_esquerda(matriz, peca, x, y): #funçao que limpa a peça e verifica se a posiçao da esquerda está livre. 
      limparpeca(matriz, peca, x, y)
      if not Pode_mover(matriz, peca, x, y - 1): 
        y -= 1  #caso ela possa mover a posição das colunas recebe menos 1.
      return y  #retorna a nova posição

def rotacionar_peca(peca): #função retorna a peça rotacionada.
    return [list(reversed(y)) for y in zip(*peca)]

def rotacionar_e_inserir(matriz, peca, x, y): #função usa a rotaçao de peça, verifica se tem espaço para girar, limpa a peça e retorna ela na forma rotacionada.
    nova_peca = rotacionar_peca(peca)
    limparpeca(matriz, peca, x, y)  
    if not Pode_mover(matriz, nova_peca, x, y):  
        peca = nova_peca  
    return peca 

def tempojg(s): #função para controlar o tempo de queda das peças que pode ser alternado.
    time.sleep(s)
    

def limparpeca(matriz, peca, x, y): #função que verifica os blocos da peça e transforma eles em blocos do fundo
     for i in range(len(peca)):
        for j in range(len(peca[i])):
            if peca[i][j] != '⬛':  
                matriz[x + i][y + j] = '⬛'

def gerar_nova_peca(): #essa função puxa uma peça aleatoria e sorteia uma rotação para ser inserida no jogo.
    peça = random.choice(peças)
    peçaramdom = rotacionar_peca(peça)
    peçaramdom2 = rotacionar_peca(peçaramdom)
    sorte = random.randint(1, 4)
    if sorte == 1:
        return peçaramdom
    elif sorte == 2:
        return peçaramdom2
    elif sorte == 3:
        peçaramdom3 = rotacionar_peca(peçaramdom2)
        return peçaramdom3
    else:
        return peça
 

def KABUM(matriz, peca, x, y): #essa função verifica se a peça inserida é a bomba.
    if peca == [['⬛','⬛','⬛'], ['⬛','💣','⬛'],['⬛','⬛','⬛']]:
        if not Pode_mover(matriz, peca, x, y): #verifica se a bomba esta inserida.
            for i in range(len(peca)):
                for j in range(len(peca[i])):
                    if 0 <= x + i < len(matriz) and 0 <= y + j < len(matriz[0]):
                        if matriz[x+i][y+j] != '⬛': #transforma todo o range da peça em blocos pretos
                            matriz[x+i][y+j] = '⬛'
            return True    
    return False

def reset():
    verifica = True
    while verifica == True:
        again = input('Jogar novamente?(S/N)').strip().upper()
        if again == 'S':
                resp = 'S'
                return resp
        elif again == 'N':
                resp = 'N'
                return resp
        else: 
            print('Resposta ivalida tente novamente.')

peças = [ #lista de peças
    
    [['🟩', '🟩', '🟩', '🟩']], #peça I
    [['🟩', '🟩'], ['🟩', '🟩']], #peça O
    [['🟩','🟩', '🟩'], ['⬛', '🟩', '⬛']], #peça T 
    [['🟩', '🟩', '⬛'], ['⬛', '🟩', '🟩']], #peça Z
    [['⬛', '🟩','🟩'], ['🟩', '🟩', '⬛']],  #peça S
    [['⬛', '⬛', '🟩'], ['🟩', '🟩', '🟩']], #peça L
    [['🟩', '⬛', '⬛'], ['🟩', '🟩', '🟩']],  #peça J
    [['⬛','⬛','⬛'], ['⬛','💣','⬛'],['⬛','⬛','⬛']]#BOMBA
]

resp = 'S'
while resp == 'S':

    #definiçoes iniciais:
    matriz = criarmatriz(20, 10) #tabuleiro 20x10
    peca = gerar_nova_peca() #peça inicial
    x, y = 0, random.randint(0,7)  #posiçoes iniciais
    verifica = True #verificação do loop do jogo
    pontuação = 0 #pontuação inicial

    while verifica == True: #loop do jogo
        print(f'{'-='*40}' #print dos controles do jogo
            '\nCONTROLES: w(girar), s(acelerar), a(esquerda), d(direita)')
        print(  #pontuação que vai se atualizando
            f'{'-='*40}'
            f'\nPONTOS: {pontuação}'
            )
        if keyboard.is_pressed('s'):
            tempojg(0.1)
        else:                #uso do keyboard para chamar as funções de movimento das peças
            tempojg(0.5)
        if keyboard.is_pressed('a'):
            y = mover_esquerda(matriz, peca, x, y)
        if keyboard.is_pressed('d'):
            y = mover_direita(matriz, peca, x, y)
        if keyboard.is_pressed('w'):  
            peca = rotacionar_e_inserir(matriz, peca, x, y)

        limparpeca(matriz, peca, x, y) #limpa a peça para ela ser movida
        
        if not Pode_mover(matriz, peca, x + 1, y): #equanto não houver colisão a posição x vai se atualizando.
            x = mover_baixo(matriz, peca, x, y)

        else:  #após a peça colidir
            if KABUM(matriz, peca, x, y):   #chama a função da bomba caso a peça for ela, e gera a proxima peça
                peca = gerar_nova_peca()   
                x, y = 0, random.randint(2, 6)

            else:    
                inserirpeca(matriz, peca, x, y) #no caso das outras peças elas são fixadas e uma nova é gerada
                peca = gerar_nova_peca()
                x, y = 0, random.randint(2,6) 
                pontuação += remove_linha(matriz) #pontuação atualizada
                remove_linha(matriz) #remove as linhas preenchidas
            
            if Pode_mover(matriz, peca, x, y): #o loop é parado quando a peça gerada não se move indicando que a linha do topo esta ocupada
                verifica = False

        
        
        printmatriz(matriz) 
        
    
    print("Game Over!")
    
    resp = reset()
print('Obrigado por jogar!\nAté a proxima!!')
    