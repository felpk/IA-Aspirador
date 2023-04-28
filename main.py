from collections import deque

sujo = 1
limpo = 0

posicao = [1, 1]    #posicao inicial

table = [
    [[(0, 0), sujo],  [(0, 1), sujo],  [(0, 2), limpo]],
    [[(1, 0), limpo], [(1, 1), sujo], [(1, 2), sujo]],
    [[(2, 0), sujo],  [(2, 1), limpo], [(2, 2), sujo]]
]


# Função que move a posição do aspirador de pó na matriz
def mover(direção, posição_atual):
    if direção == 'norte':
        posição_atual[0] -= 1
        print('moveu-se ao norte')
        
    elif direção == 'oeste':
        posição_atual[1] += 1
        print('moveu-se ao oeste')
    
    elif direção == 'leste':
        posição_atual[1] -= 1
        print('moveu-se ao leste')
    
    elif direção == 'sul':
        posição_atual[0] += 1
        print('moveu-se ao sul')
        
    # Verifica se a posição atual ultrapassa os limites da matriz
    if posição_atual[0] == -1:
        posição_atual[0] += 1
    if posição_atual[1] == -1:
        posição_atual[1] += 1
    
    # Retorna a nova posição do aspirador de pó
    return posição_atual


# Função que limpa a posição atual na matriz, se ela estiver suja
def aspirar(posição_atual, table):

    i, j = posição_atual[0], posição_atual[1]

    # Verifica se a posição atual está limpa ou suja
    if table[i][j][1] == 0:
        print(f'Espaço [{i, j}] já está limpo!\n')

    elif table[i][j][1] == 1:
        # Limpa a posição atual
        table[i][j][1] = 0
        print(f'Espaço [{i, j}] Aspirado!\n')
    
    # Retorna a matriz atualizada
    return table


# Função que imprime a matriz ambiente na tela
def imprimir_ambiente(table):
    for i in range(len(table)):
        print(table[i])
    print()


# Função que encontra todas as posições sujas na matriz
def sensor_sujos(table):
    sujos = []
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j][1] == 1:
                sujos.append((i, j))
    return sujos



def limpar_ambiente(posicao, table):
    # Encontrar todas as células sujas
    sujos = sensor_sujos(table)
    
    # Criar uma matriz para marcar as células já visitadas
    visitado = [[False] * len(table[i]) for i in range(len(table))]
    
    # Criar uma matriz para armazenar as distâncias a partir da posição atual
    distancia = [[float('inf')] * len(table[i]) for i in range(len(table))]
    
    # Definir a posição inicial e marcar como visitado
    i, j = posicao[0], posicao[1]
    visitado[i][j] = True
    distancia[i][j] = 0
    
    # Iniciar a fila com a posição inicial
    fila = deque([(i, j)])
    
    # Enquanto a fila não estiver vazia
    while fila:
        # Remover o primeiro elemento da fila e definir como posição atual
        i, j = fila.popleft()
        
        # Se a posição atual for uma célula suja, aspirar
        if (i, j) in sujos:
            aspirar([i, j], table)
            
        # Para cada célula adjacente à posição atual
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            
            # Se a célula adjacente estiver dentro da matriz e não tiver sido visitada
            if 0 <= ni < len(table) and 0 <= nj < len(table[ni]) and not visitado[ni][nj]:
                # Marcar como visitado e calcular a distância a partir da posição atual
                visitado[ni][nj] = True
                distancia[ni][nj] = distancia[i][j] + 1
                
                # Adicionar a célula adjacente à fila
                fila.append((ni, nj))
    
    # Imprimir a matriz ambiente após a limpeza
    imprimir_ambiente(table)
    
    
   
    


limpar_ambiente(posicao, table)
'''teste = ['norte',  #0, 1
         'norte',  #0, 1
         'direita', #0, 2
         'sul',    #1, 2
         'sul',    #2, 2
         'esquerda', #2, 1
         'norte',  #1, 1
         'esquerda']#1, 0


imprimir_ambiente(table)
sujos = encontrar_sujos(table)
print(sujos)

for i, pos in enumerate(teste):
    posicao = mover(pos, posicao)
    #print(posicao)
    table = aspirar(posicao, table)

imprimir_ambiente(table)'''