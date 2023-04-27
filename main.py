sujo = 1
limpo = 0

posicao = [1, 1]    #posicao inicial
table = [
    [(1,1), sujo], [(1,2), sujo], [(1,3), limpo],
    [(2,1), limpo], [(2,2), limpo], [(2,3), sujo],
    [(3,3), sujo], [(3,2), limpo], [(3,3), sujo]
]

orientacao = 'oeste'   #orientacao inicial

def mover_frente():
    if orientacao == 'norte':
        posicao[0] -= 1

    elif orientacao == 'leste':
        posicao[1] += 1

    elif orientacao == 'oeste':
        posicao[1] -= 1

    elif orientacao == 'sul':
        posicao[0] += 1
        
    print(posicao)

def girar_direita():
    global orientacao
    if orientacao == 'norte':
        orientacao = 'oeste'

    elif orientacao == 'oeste':
        orientacao = 'sul'

    elif orientacao == 'sul':
        orientacao = 'leste'

    elif orientacao == 'leste':
        orientacao = 'norte'

    print(orientacao)

def aspirar():
    global i
    global j 
    i = posicao[0]
    j = posicao[1]

    if table[i][j] == limpo:
        print(f'Espaço [{i, j}] já está limpo!\n')

    elif table[i][j] == sujo:
        table[i][j] = limpo
        print(f'Espaço [{i, j}] limpo!\n')

