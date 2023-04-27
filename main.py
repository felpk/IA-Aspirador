sujo = 1
limpo = 0
i = 1
j = 1
posicao = [1, 1]    #posicao inicial
#orientacao = 'norte'   #orientacao inicial
table = [
    [(0, 0), sujo], [(0, 1), sujo], [(0, 2), limpo],
    [(1, 0), limpo], [(1, 1), limpo], [(1, 2), sujo],
    [(2, 0), sujo], [(2, 1), limpo], [(2, 2), sujo]
]

def mover(direção, posição_atual):
    if direção == 'frente':
        posição_atual[0] -= 1
        
    elif direção == 'direita':
        posição_atual[1] += 1
    
    elif direção == 'esquerda':
        posição_atual[1] -= 1
    
    elif direção == 'tras':
        posição_atual[0] += 1
        
        
    if posição_atual[0] == -1:
        posição_atual[0] += 1
    if posição_atual[1] == -1:
        posição_atual[1] += 1
        
    
    return posição_atual


teste = ['frente',  #0, 1
         'frente',  #0, 1
         'direita', #0, 2
         'tras',    #1, 2
         'tras',    #2, 2
         'esquerda', #2, 1
         'frente',  #1, 1
         'esquerda']#1, 0
aspirador = posicao


for i, pos in enumerate(teste):
    aspirador = mover(pos, aspirador)
    print(aspirador)

