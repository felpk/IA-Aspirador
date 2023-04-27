sujo = 1
limpo = 0

posicao = [1, 1]    #posicao inicial
posicao_atual = posicao #posicao atual

table = [
    [(0, 0), sujo],  [(0, 1), sujo],  [(0, 2), limpo],
    [(1, 0), limpo], [(1, 1), limpo], [(1, 2), sujo],
    [(2, 0), sujo],  [(2, 1), limpo], [(2, 2), sujo]
]



def mover(direção, posição_atual):
    if direção == 'norte':
        posição_atual[0] -= 1
        
    elif direção == 'direita':
        posição_atual[1] += 1
    
    elif direção == 'esquerda':
        posição_atual[1] -= 1
    
    elif direção == 'sul':
        posição_atual[0] += 1
        
        
    if posição_atual[0] == -1:
        posição_atual[0] += 1
    if posição_atual[1] == -1:
        posição_atual[1] += 1
    
    return posição_atual



def aspirar(posição_atual, table):

    i, j = posição_atual[0], posição_atual[1]

    if table[i][j][1] == 0:
        print(f'Espaço [{i, j}] já está limpo!\n')

    elif table[i][j][1] == 1:
        table[i][j][1] = 0
        print(f'Espaço [{i, j}] Aspirado!\n')
        

# for i, pos in enumerate(teste):
#     aspirador = mover(pos, aspirador)
#     print(aspirador)

def imprimir_ambiente():    # Imprimir matriz ambiente onde 0 é limpo e 1 é sujo Funcionando
    print()
    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            print(table[index][1], end=' ')
        print()
    print()



teste = ['frente',  #0, 1
         'frente',  #0, 1
         'direita', #0, 2
         'tras',    #1, 2
         'tras',    #2, 2
         'esquerda', #2, 1
         'frente',  #1, 1
         'esquerda']#1, 0


for i, pos in enumerate(teste):
    posicao = mover(pos, posicao)
    #print(aspirador)
    aspirar(posicao, table)
