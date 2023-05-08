sujo = 1
limpo = 0

posicao = [1, 1]    #posicao inicial
posicao_atual = posicao #posicao atual

qtd_movimentos = 0
qtd_aspirar = 0

table = [
    [[(0, 0), sujo],  [(0, 1), sujo],  [(0, 2), limpo]],
    [[(1, 0), limpo], [(1, 1), sujo], [(1, 2), sujo]],
    [[(2, 0), sujo],  [(2, 1), limpo], [(2, 2), sujo]]
]



def mover(direção, posição_atual, table):
    global qtd_movimentos

    if direção == 'norte':
        posição_atual[0] -= 1
        print(f'moveu-se para o norte ^')#, end='')
        
    elif direção == 'oeste':
        posição_atual[1] += 1
        print(f'moveu-se para a direita >')#, end='')
    
    elif direção == 'leste':
        posição_atual[1] -= 1
        print(f'moveu-se para a esquerda <')#, end='')
    
    elif direção == 'sul':
        posição_atual[0] += 1
        print(f'moveu-se para o sul v')#, end='')
        
    # Verifica se a posição atual ultrapassa os limites da matriz
    if posição_atual[0] == -1:
        posição_atual[0] += 1
    if posição_atual[1] == -1:
        posição_atual[1] += 1
    
    qtd_movimentos = qtd_movimentos + 1
    mostar_andando(table, posição_atual)
    #print(f'{posição_atual}\n')
    return posição_atual




def imprimir_ambiente(table):    # Imprimir matriz ambiente onde 0 é limpo e 1 é sujo Funcionando
    for i in range(len(table)):
        print(table[i])
    print()



def mostar_andando(table, posição_atual):
    i, j = posição_atual
    table[i][j].append('x')
    imprimir_ambiente(table)
    table[i][j].remove('x')


def buscar_sujos(table):
    global sujos
    sujos = []
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j][1] == 1:
                sujos.append((i, j))
    return sujos


def mover_para(posicao_atual, posicao_destino, table):
    direcao_norte = 'norte'
    direcao_sul = 'sul'
    direcao_esquerda = 'leste'
    direcao_direita = 'oeste'
    nova_posicao = posicao_atual.copy()

    # Movendo o aspirador norte/sul para chegar na posição destino
    while nova_posicao[0] != posicao_destino[0]:
        if nova_posicao[0] < posicao_destino[0]:
            nova_posicao = mover(direcao_sul, nova_posicao, table)
        else:
            nova_posicao = mover(direcao_norte, nova_posicao, table)

    # Movendo o aspirador na horizontal para chegar na posição destino
    while nova_posicao[1] != posicao_destino[1]:
        if nova_posicao[1] < posicao_destino[1]:
            nova_posicao = mover(direcao_direita, nova_posicao, table)
        else:
            nova_posicao = mover(direcao_esquerda, nova_posicao, table)

    return nova_posicao


def eficiencia(qtd_movimentos, qtd_aspirar):
    if qtd_aspirar != 0:
        return (f'Qtd movimentos: {qtd_movimentos}\nQtd aspirações: {qtd_aspirar}\n{qtd_aspirar/qtd_movimentos * 100} %')
    else: 
        return f'Quantidade de movimentos é {qtd_movimentos}.'
    
    
def aspirar(posição_atual, table):
    global qtd_aspirar

    i, j = posição_atual[0], posição_atual[1]

    if table[i][j][1] == 0:
        print(f'Espaço [{i, j}] já está limpo!\n')

    elif table[i][j][1] == 1:
        table[i][j][1] = 0
        print(f'Espaço [{i, j}] Aspirado!\n')
        qtd_aspirar += 1


    return table

def encontrar_aspirar_sujos(table):
    posicao_atual = [1, 1]
    global qtd_aspirar
    global qtd_movimentos
    print(f'posicao inicial: {posicao_atual}')
    for i in range(len(table)):           # Itera pelos elementos da table

        for j in range(len(table[i])):      # Itera dentro de cada elemento da table
            if table[i][j][1] == 1:         # Se quadrado atual == sujo                                 
                posicao_atual = mover_para(posicao_atual, [i, j], table)
                print("Posição atual:", posicao_atual)
                table = aspirar(posicao_atual, table)
    return qtd_aspirar

#execução

imprimir_ambiente(table)
sujos = buscar_sujos(table)
encontrar_aspirar_sujos(table, sujos)
imprimir_ambiente(table)

print(eficiencia(qtd_movimentos, qtd_aspirar))