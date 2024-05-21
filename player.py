#!/usr/bin/env python3
"""
Implemente aqui o seu código para o jogador.

Seu principal objetivo é implementar a função `player`, que deve retornar uma lista de 4 cores, o seu próximo palpite.
Como exemplo, a função abaixo retorna um palpite aleatório.

Dicas:
- Você pode implementar outras funções para auxiliar a função `player`.
- Você pode salvar informações entre os palpites usando variáveis globais (fora de qualquer função).
"""
from colors import *
from random import sample


# Cores disponíveis para o palpite
colors = [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE]
cores_adicionais = [ORANGE, BLACK, WHITE]

cor_tirada = 0
cor_colocada = 0

cores_certas = []
cores_erradas = []
cores_poss = []

indice_subst = 0
indice_cadicional = 0

quantidade_certa = 0

'''Dicionario que armazena: na primeira lista, as posicoes certas das cores e 
a segunda armazena as posiveis posicoes das cores'''
dic_cores = {
    RED:[0,1,2,3],
    GREEN:[0,1,2,3],
    BLUE:[0,1,2,3],
    YELLOW:[0,1,2,3],
    ORANGE:[0,1,2,3],
    BLACK:[0,1,2,3],
    WHITE:[0,1,2,3],
}
dic_posicoes = {
    0: [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE],
    1: [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE],
    2: [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE],
    3: [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE]

} #TESTE

pares_trocas = [] #Lista de pares trocados na permutacao
pares_n_trocas = [] #Lista de pares nao trocados na permutacao
dif_pos = [] #Lista que salva a diferenca entre o acerto das posicoes corretas entre a ultima e a penultima tentativa
dif_cor = [] #Lista que salva a diferenca entre o acerto das posicoes corretas entre a ultima e a penultima tentativa
pos_corretas = [] #Listas que armazena quais posicoes foram encontradas
pos_restantes = [] #Listas que armazena quais posicoes nao foram encontradas

indice_cores = 0
limitante = 0 #contador que será utulizado para limitar uma ação a ser realizada apenas uma vez, durante a retirada das cores erradas
posicao_esperada = [0] #Lista que indica os valore esperados para a quantidade de cores nas posições corretas, sendo 0 no primeiro palpite

def player(guess_hist, res_hist):

    global indice_subst
    global indice_cadicional
    global cor_tirada
    global cor_colocada
    global colors
    global cores_adicionais
    global cores_erradas
    global cores_certas
    global cores_poss
    global quantidade_certa

    global dif_pos
    global dif_cor
    global dic_cores
    global limitante

    global pares_trocas
    global pares_n_trocas
    global pos_corretas
    global pos_restantes

    global dic_posicoes
    global dic_cores
    global posicao_esperada
    global indice_cores

    if len(guess_hist)==0:
        # Cores disponíveis para o palpite
        colors = [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE]
        cores_adicionais = [ORANGE, BLACK, WHITE]

        cor_tirada = 0
        cor_colocada = 0

        cores_certas = []
        cores_erradas = []
        cores_poss = []

        indice_subst = 0
        indice_cadicional = 0

        quantidade_certa = 0

        '''Dicionario que armazena: na primeira lista, as posicoes certas das cores e 
        a segunda armazena as posiveis posicoes das cores'''
        dic_cores = {
            RED:[0,1,2,3],
            GREEN:[0,1,2,3],
            BLUE:[0,1,2,3],
            YELLOW:[0,1,2,3],
            ORANGE:[0,1,2,3],
            BLACK:[0,1,2,3],
            WHITE:[0,1,2,3],
        }
        dic_posicoes = {
            0: [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE],
            1: [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE],
            2: [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE],
            3: [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE]

        } #TESTE

        pares_trocas = [] #Lista de pares trocados na permutacao
        pares_n_trocas = [] #Lista de pares nao trocados na permutacao
        dif_pos = [] #Lista que salva a diferenca entre o acerto das posicoes corretas entre a ultima e a penultima tentativa
        dif_cor = [] #Lista que salva a diferenca entre o acerto das posicoes corretas entre a ultima e a penultima tentativa
        pos_corretas = [] #Listas que armazena quais posicoes foram encontradas
        pos_restantes = [] #Listas que armazena quais posicoes nao foram encontradas

        indice_cores = 0
        limitante = 0 #contador que será utulizado para limitar uma ação a ser realizada apenas uma vez, durante a retirada das cores erradas
        posicao_esperada = [0] #Lista que indica os valore esperados para a quantidade de cores nas posições corretas, sendo 0 no primeiro palpite
            
    """
    Função principal do jogador.

    Esta função deve retornar o seu palpite, que deve ser uma lista de 4 cores.
    As cores disponíveis são: RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE.

    Parâmetros:
    - guess_hist: lista de palpites anteriores
    - res_hist: lista de resultados anteriores

    Retorna:
    - lista de 4 cores

    Exemplo:
    return [RED, GREEN, BLUE, YELLOW]
    """

    '''global indice_subst
    global indice_cadicional
    global cor_tirada
    global cor_colocada

    global cores_erradas
    global cores_certas
    global cores_poss
    global quantidade_certa

    global dif_pos
    global dif_cor
    global dic_cores'''

    acao = 0

    #Armazenando os dados de cada tentativa
    if len(guess_hist) == 1:
        analise(guess_hist,res_hist)
    elif len(guess_hist) > 1:
        #Diferença entre os valores das posições:
        dif_pos.append(res_hist[-1][1] - res_hist[-2][1])
        #Diferenca entre os valores das cores
        dif_cor.append(res_hist[-1][0] - res_hist[-2][0])
        analise(guess_hist, res_hist, dif_cor[-1], dif_pos[-1]) #INTEGRAR
    #fazendo a nova tentativa

    if len(guess_hist) == 0: #caso inicial
        palpite = [RED, GREEN, BLUE, YELLOW]
        return palpite
    else:
        palpite = guess_hist[-1].copy()

        if len(cores_erradas) == 3:
            cores_certas = []
            for cor in colors:
                if cor not in cores_erradas:
                    cores_certas.append(cor)
        
        if len(cores_poss) == 4:
            cores_certas = cores_poss
            cores_poss = []
        
        if res_hist[-1][0] != 4 and len(cores_certas) < 4: #se for 4 então não é necessario seguir em frente

            if len(guess_hist) == 1:
                cor_tirada = colors[indice_subst]
                cor_colocada = cores_adicionais[indice_cadicional]

                palpite = achar_substituir(palpite, cor_colocada, cor_tirada)

            else:
                diff = res_hist[-1][0] - quantidade_certa

                if diff == 0:
                    acao = 0

                elif diff == -1:
                    acao = -1

                else:
                    acao = 1

                if acao == 0:

                    cores_poss.append(cor_tirada)

                    if cor_colocada not in cores_poss:
                        cores_poss.append(cor_colocada)

                    indice_subst += 1

                    if len(cores_poss) == 4:

                        cores_certas = cores_poss
                        cores_poss = []
                        palpite = substituir_lista(palpite, cores_certas)
                        cores_certas = palpite
                    

                    elif len(cores_poss) + len(cores_erradas) > 3 and len(cores_poss) + len(cores_certas) == 4:

                        cores_certas += cores_poss
                        cores_poss = []
                        palpite = substituir_lista(palpite, cores_certas)
                        cores_certas = palpite

                    elif len(cores_poss) + len(cores_certas) > 4:
                        cores_erradas += cores_poss
                        cores_certas = []

                        for cor in colors:
                            if cor not in cores_erradas:
                                cores_certas.append(cor)
                                
                        palpite = substituir_lista(palpite, cores_certas)
                        cores_certas = palpite
                        
                    else:
                        palpite = achar_substituir(palpite, cor_tirada, cor_colocada)

                        cor_tirada = colors[indice_subst]
                        cor_colocada = cores_adicionais[indice_cadicional]

                        palpite = achar_substituir(palpite, cor_colocada, cor_tirada)

                elif acao == -1:

                    cores_erradas += cores_poss #cores erradas que haviam sido colocadas para avaliação quando diff == 0
                    cores_poss = []
                    cores_certas.append(cor_tirada)

                    if cor_colocada not in cores_erradas: #cor errada sem que antes tenha tido diff == 0
                        cores_erradas.append(cor_colocada) 

                    indice_subst += 1
                    indice_cadicional += 1
                    
                    if len(cores_erradas) == 3:
                        cores_certas = []
                        for cor in colors:
                            if cor not in cores_erradas:
                                cores_certas.append(cor)
                        palpite = substituir_lista(palpite, cores_certas)
                        cores_certas = palpite
                    
                    else:

                        palpite = achar_substituir(palpite, cor_tirada, cor_colocada) #cor tirada estava correta

                        cor_tirada = colors[indice_subst]
                        cor_colocada = cores_adicionais[indice_cadicional]

                        palpite = achar_substituir(palpite, cor_colocada, cor_tirada)

                elif acao == 1:

                    cores_certas += cores_poss
                    cores_poss = []
                    
                    cores_erradas.append(cor_tirada)

                    if cor_colocada not in cores_certas:
                        cores_certas.append(cor_colocada)
                        
                    indice_subst += 1
                    indice_cadicional += 1

                    if len(cores_erradas) == 3:      

                        cores_certas = []
                        for cor in colors:
                            if cor not in cores_erradas:
                                cores_certas.append(cor)

                        palpite = substituir_lista(palpite, cores_certas)
                        cores_certas = palpite

                    elif len(cores_certas) == 4:
                        
                        palpite = substituir_lista(palpite, cores_certas)
                        cores_certas = palpite

                    else:
                        cor_tirada = colors[indice_subst]
                        cor_colocada = cores_adicionais[indice_cadicional]

                        palpite = achar_substituir(palpite, cor_colocada, cor_tirada)

        if res_hist[-1][0] > quantidade_certa:
            quantidade_certa = res_hist[-1][0]



        if len(dif_cor) > 1: 
            analise(guess_hist, res_hist, dif_cor[-1], dif_pos[-1])
        if res_hist[-1][0] < 4 and len(cores_certas) < 4:
            #Usando os dados captados durante as analises para escolher uma sequencia otima das coress
            if len(cores_certas) > 0:
                #Trocando cores de posições antes das 4 cores serem adivinhadas
                for cor in cores_certas:
                    if cor in palpite and cor not in dic_posicoes[indice_da_cor(palpite,cor)]:
                        for troca in dic_posicoes[indice_da_cor(palpite,cor)]:
                            if troca in palpite:
                                return permutacao(palpite, indice_da_cor(palpite,cor), indice_da_cor(palpite, troca))
                        #Trocar a cor desejada com uma cor errada, com uma cor que também está na posição errada e que possa estar na sua posição
            #Caso a posição de uma cor já tenha sido descoberta, colocá-la nesta posição
            copia_palpite = palpite.copy
            for posicao in dic_posicoes:
                if len(dic_posicoes[posicao]) == 1 and indice_da_cor(palpite, dic_posicoes[posicao][0]) != posicao:
                    palpite = permutacao(palpite,posicao, indice_da_cor(palpite, dic_posicoes[posicao][0]))
            #Retirar as cores que se encontram em posições erradas
            for posicao in range(4):
                if palpite[posicao] not in dic_posicoes[posicao]:
                    for i in range(len(dic_posicoes[posicao])):
                        if dic_posicoes[posicao][i] in palpite and dic_posicoes[posicao][i] in dic_posicoes[indice_da_cor(palpite, dic_posicoes[posicao][i])]:
                            palpite = permutacao(palpite, posicao, indice_da_cor(palpite, dic_posicoes[posicao][i]))
                    
            return palpite

    #Após achar as 4 cores, buscar as posições corretas
    if len(res_hist) > 0 and res_hist[-1][0] == 4 or len(cores_certas) == 4:
        '''global limitante'''

        if res_hist[-1][0] == 4: 
            cores_certas = guess_hist[-1]
        #TESTE
        #Retirar as cores erradas do dicionário de posição e de cor, restringindo o loop a uma única execução 
        
        copia_lista = 0
        if limitante == 0:
            for posicao in  dic_posicoes:
                copia_lista = dic_posicoes[posicao].copy()
                for cor in copia_lista:
                    
                    if cor not in cores_certas:
                        dic_posicoes[posicao].remove(cor)
            if len(cores_certas) == 4:
                limitante = 1
            #Atualizar o dicionário de posições com as posições já encontradas
            for cor in dic_cores:
                if cor in cores_certas and type(dic_cores[cor]) == int:
                    dic_posicoes[dic_cores[cor]] = [cor]
        
        '''global pares_trocas
        global pares_n_trocas
        global pos_corretas
        global pos_restantes'''
        escolha1 = 0
        escolha2 = 0

        #Alterando as informações do dicionário quando há diferença entre os valores
        if len(res_hist) > 1 and res_hist[-2][0] == 4:           
            if dif_pos[-1] == 2:
                #Verificar se houve apenas uma permutação
                if guess_hist[-1][pares_n_trocas[-1][0]] == guess_hist[-2][pares_n_trocas[-1][0]] and guess_hist[-1][pares_n_trocas[-1][1]] == guess_hist[-2][pares_n_trocas[-1][1]]:
                    #Se aumentarem as posições corretas em 2, devemos trocas o par não permutado da última tentativa
                    for i in range(2):
                        dic_cores[guess_hist[-1][pares_trocas[-1][i]]] = pares_trocas[-1][i]
                        dic_posicoes[pares_trocas[-1][i]] = [guess_hist[-1][pares_trocas[-1][i]]] #TESTE

                        dic_cores[guess_hist[-1][pares_n_trocas[-1][i]]] = pares_n_trocas[-1][(i+1)%2]
                        dic_posicoes[pares_n_trocas[-1][(i+1)%2]] = [guess_hist[-1][pares_n_trocas[-1][i]]] #TESTE
                
            
            elif dif_pos[-1] == -2:
                #Se diminuírem as posições corretas em 2, devemos trocas o par não permutado da penúltima tentativa
                for i in range(2):
                    dic_cores[guess_hist[-2][pares_trocas[-1][i]]] = pares_trocas[-1][i]
                    dic_posicoes[pares_trocas[-1][i]] = [guess_hist[-2][pares_trocas[-1][i]]] #TESTE

                    #dic_cores[cores_certas[pares_trocas[-2][i]]] = pares_trocas[-2][i]
                    

            #Caso a diferença entre as posições não tenha se alterado, ambas as cores trocadas estão em posições erradas, no último e no penúltimo palpite
            elif dif_pos[-1] == 0:
                #Retirando as posições nas quais as cores estão erradas
                for i in range(2):
                    if type(dic_cores[cores_certas[pares_trocas[-1][i]]]) == list and pares_trocas[-1][i] in dic_cores[cores_certas[pares_trocas[-1][i]]]:
                        remover(guess_hist[-1][pares_trocas[-1][i]], pares_trocas[-1][i])
                        #dic_cores[guess_hist[-1][pares_trocas[-1][i]]].remove(pares_trocas[-1][i])
                        

                    if type(dic_cores[guess_hist[-2][pares_trocas[-1][(i+1)%2]]]) == list and pares_trocas[-1][(i+1)%2] in dic_cores[guess_hist[-2][pares_trocas[-1][(i+1)%2]]]:
                        remover(guess_hist[-2][pares_trocas[-1][(i+1)%2]], pares_trocas[-1][(i+1)%2])
                    '''if type(dic_cores[guess_hist[-2][pares_trocas[-2][i]]]) == list and len(pares_trocas) > 1 and pares_trocas[-2][i] in dic_cores[guess_hist[-2][pares_trocas[-2][i]]]:
                        remover(guess_hist[-2][pares_trocas[-2][i]], pares_trocas[-2][i])
                        #dic_cores[guess_hist[-2][pares_trocas[-2][i]]].remove(pares_trocas[-2][i])'''
                        

            
            
            elif dif_pos[-1] == 1:
                #Se houve um aumento da posição, ambas as cores estavam em posições erradas no penúltimo palpite
                if len(pares_trocas) > 0:
                    for i in range(2):
                        if type(dic_cores[guess_hist[-2][pares_trocas[-1][i]]]) == list and pares_trocas[-1][i] in dic_cores[guess_hist[-2][pares_trocas[-1][i]]]:
                            remover(guess_hist[-2][pares_trocas[-1][i]], pares_trocas[-1][i])
                            #dic_cores[guess_hist[-2][pares_trocas[-1][i]]].remove(pares_trocas[-1][i])
                        
                
                                #TOMAR CUIDADO COM O PAR TROCA, É PRECISO VERIFICAR SE ELE ESTÁ SE REFERINDO PARA A COR DESEJADA, ACHAR OUTRO MÉTODO DE VERIFICAÇÃO
            else:
                #Se houve um aumento da posição, ambas as cores estavam em posições erradas no último palpite
                for i in range(2):
                    if type(dic_cores[cores_certas[pares_trocas[-1][i]]]) == list:
                        if pares_trocas[-1][i] in dic_cores[cores_certas[pares_trocas[-1][i]]]:
                            remover(guess_hist[-1][pares_trocas[-1][i]], pares_trocas[-1][i])
                            #dic_cores[guess_hist[-1][pares_trocas[-1][i]]].remove(pares_trocas[-1][i])
                        #Caso uma das cores não estivesse em uma posição possível antes da troca, a outra cor que foi trocada estava na posição correta
                        if type(dic_cores[guess_hist[-2][pares_trocas[-1][i]]]) == list and pares_trocas[-1][i] not in dic_cores[guess_hist[-2][pares_trocas[-1][i]]]:
                            dic_cores[guess_hist[-2][pares_trocas[-1][(i+1)%2]]] = pares_trocas[-1][(i+1)%2]
                            dic_posicoes[pares_trocas[-1][(i+1)%2]] =  [guess_hist[-2][pares_trocas[-1][(i+1)%2]]] #TESTE

                        
                



        #Retirando as posicoes ja encontradas:
        copia_dic = dic_cores.copy()
    
        for i in copia_dic:
            if type(copia_dic[i]) == int and i in cores_certas:
                for k in copia_dic:
                    if type(copia_dic[k]) == list and copia_dic[i] in copia_dic[k]:
                        remover(k,copia_dic[i])
        #Realizando uma atualização da anaálise antes
        if len(dif_cor) > 0:
            analise(guess_hist, res_hist, dif_cor[-1], dif_pos[-1])

        #Colocando as cores em suas posições já encontradas
        contador = 0
        #Criar uma cópia das cores certas para poder manipular a original para preservar a sequência
        copia_cores = cores_certas.copy()
        while contador < 4:
            if cores_certas[contador] not in dic_posicoes[contador]:
                if len(dic_posicoes[contador]) == 1:
                    #Realizando a troca entre uma cor com posição encontrada e outra cuja posição é desconhecida
                    '''if cores_certas[contador] in dic_posicoes[indice_da_cor(cores_certas,dic_posicoes[contador][0])]:'''
                    '''type(dic_cores[cores_certas[contador]]) == list and contador in dic_cores[cores_certas[contador]]:'''
                    for troca in dic_posicoes[contador]:
                            if troca in cores_certas:
                                cores_certas = permutacao(cores_certas, contador, indice_da_cor(cores_certas, troca))
                                break
                    '''cores_certas = permutacao(cores_certas,contador,indice_da_cor(cores_certas,dic_posicoes[contador][0]))'''
                    '''if cores_certas[indice_da_cor(cores_certas,dic_posicoes[contador][0])] in indice_da_cor(cores_certas,dic_posicoes[contador][0]):
                        remover(cores_certas[indice_da_cor(cores_certas,dic_posicoes[contador][0])], indice_da_cor(cores_certas,dic_posicoes[contador][0]))'''
                    '''if cores_certas[pares_trocas[-1][1]] in pares_trocas[-1][1]:
                            remover(cores_certas[pares_trocas[-1][1]], pares_trocas[-1][1])'''
                    '''else:
                        if type(dic_cores[cores_certas[contador]]) == list and 
                        cores_certas = permutacao(cores_certas, contador,  )'''
            contador += 1
           
           
           
           
           
           
            '''if contador != dic_cores[cores_certas[contador]]:

                if type(dic_cores[copia_cores[contador]]) == int:
                    #Realizando a troca entre uma cor com posição encontrada e outra cuja posição é desconhecida
                    if type(dic_cores[cores_certas[dic_cores[cores_certas[contador]]]]) == list:           
                        cores_certas = permutacao(cores_certas, contador, dic_cores[cores_certas[contador]])
                        #Removendo a posição da cor cujo valor no dicionário é representado como lista, já que a cor na qual ela está já está direcionada para outra cor
                        #O índice 
                        if pares_trocas[-1][1] in dic_cores[cores_certas[pares_trocas[-1][0]]]:
                            remover(cores_certas[pares_trocas[-1][0]], pares_trocas[-1][1])
                            
                    else:
                        cores_certas = permutacao(cores_certas, (dic_cores[cores_certas[dic_cores[cores_certas[contador]]]]), dic_cores[cores_certas[contador]])
                        if type(dic_cores[cores_certas[pares_trocas[-1][0]]]) == list and pares_trocas[-1][0] in dic_cores[cores_certas[pares_trocas[-1][0]]]:
                            remover(cores_certas[pares_trocas[-1][0]], pares_trocas[-1][0])
                            
                        contador -= 1
            contador += 1'''
                #Realizar a troca entre a posição na qual uma cor se encontra e uma possível posição na qual ela pode estar
        #Caso o palpite anterior não contemplou todas as cores
        if cores_certas != guess_hist[-1]:
            
            #Realizar uma troca de posição de uma cor que não se encontra em uma posição posição possível
            '''for cor in cores_certas:
                if type(dic_cores[cor]) == list and indice_da_cor(cores_certas,cor) not in dic_cores[cor]:
                    return permutacao(cores_certas, indice_da_cor(cores_certas,cor), dic_cores[cor][-1])'''
            if cores_certas not in guess_hist:    
                return cores_certas
            
                
       
        #Realizar a troca entre a posição na qual uma cor se encontra em uma posição que ela pode estar
        for i in range(4):
            if len(dic_posicoes[i]) > 1:
                if cores_certas[i] not in dic_posicoes[i]:
                    cores_certas = permutacao(cores_certas,i,dic_cores[cores_certas[i]][-1])
                    if cores_certas not in guess_hist:
                        return cores_certas
                          
                    '''else:
                        return permutacao(cores_certas,indice_da_cor(cores_certas, dic_posicoes[i][0]),indice_da_cor(cores_certas, dic_posicoes[i][1]))'''
                
                
                '''if type(dic_cores[cores_certas[i]]) == list and i not in dic_cores[cores_certas[i]] and len(dic_cores[cores_certas[i]]) > 0:
                    #Verificando se a cor se encontra em uma posição que ela não pode estar
                    #if i in dic_cores[cores_certas[dic_cores[cores_certas[i]][-1]]]:
                        return permutacao(cores_certas,i,dic_cores[cores_certas[i]][-1])'''
        for i in range(4):
            for troca in dic_posicoes[i]:
                if troca in cores_certas and cores_certas[i] != troca and cores_certas[i] in dic_posicoes[indice_da_cor(cores_certas,troca)]:
            
                    return permutacao(cores_certas, i, indice_da_cor(cores_certas,troca))
        
            '''if type(dic_cores[cores_certas[i]]) == list and type(dic_cores[cores_certas[dic_cores[cores_certas[i]][-1]]]) == list:
                if i in dic_cores[cores_certas[i]]:
                    if i != dic_cores[cores_certas[i]][-1] and i in dic_cores[cores_certas[dic_cores[cores_certas[i]][-1]]]:
                        return permutacao(cores_certas,i,dic_cores[cores_certas[i]][-1])
                    else:
                        return permutacao(cores_certas,i,dic_cores[cores_certas[i]][-2])'''
            
        return permutacao(cores_certas,i,(i+1)%2)
            
  
            
           


def permutacao(sequencia, indice1, indice2):
    '''
    Função que realiza permutações entre posições escolhidas dentro de uma lista
    '''
    lista_cores = sequencia.copy()
    lista_cores[indice1] = sequencia[indice2]
    lista_cores[indice2] = sequencia[indice1]
    global pares_trocas
    pares_trocas.append([indice1,indice2])
    global pares_n_trocas
    indices_faltantes = []
    for i in range(4):
        if i != indice1 and i != indice2:
            indices_faltantes.append(i)
    pares_n_trocas.append(indices_faltantes)

    return lista_cores

def indice_da_cor(lista_de_cores,cor):
    '''
    Função que acha qual o índice da cor em uma lista de cores que a contenha
    '''
    for i in range(len(lista_de_cores)):
        if lista_de_cores[i] == cor:
            return i
        

            
def analise(lista, situacao=[[0,0]], parametro1=0, parametro2=0):
    '''
    Captar informacoes das cores e suas posicoes por meio da mudanca dos valores do acerto das cores e das posicoes
    '''
    global dic_cores
    global pares_trocas
    cor_nova = 0
    cor_velha = 0
    global posicao_esperada
    
    if len(lista) > 1:
        #Armazenar qual cor foi adicionada e qual foi retirada
        
        ult_lista = set(lista[-1])
        penult_lista = set(lista[-2])
        if ult_lista != penult_lista:
            if len(ult_lista - penult_lista) == 1:
                cor_nova = (ult_lista - penult_lista).pop()
                cor_velha = (penult_lista - ult_lista).pop()

    #Determinar o valor das posições corretas esperadas
    
    i = 0
    posicao_esperada[-1] = 0
    for posicao in dic_posicoes:
            
        if len(dic_posicoes[posicao]) == 1:
            i += 1
            if lista[-1][posicao] == dic_posicoes[posicao][0]:
                posicao_esperada[-1] += 1
    posicao_esperada.append(i)
        
            
    aumento_esperado = (posicao_esperada[-1] - posicao_esperada[-2])
    if len(cores_certas) < 4 and type(cor_nova) == color:
        #Comparar se apenas houve troca de posição sem permuta
        ult = lista[-1].copy()
        ult[indice_da_cor(ult,cor_nova)] = GRAY
        penult = lista[-2].copy()
        penult[indice_da_cor(penult,cor_velha)] = GRAY
        if ult == penult:



        
            if parametro1 >= 0 and (parametro2 - aumento_esperado) > 0:               
                dic_cores[cor_nova] = (indice_da_cor(lista[-1],cor_nova))
                dic_posicoes[indice_da_cor(lista[-1],cor_nova)] = [cor_nova]
            elif parametro1 <= 0 and (parametro2 - aumento_esperado) < 0:
                dic_cores[cor_velha] = (indice_da_cor(lista[-2],cor_velha))
                dic_posicoes[indice_da_cor(lista[-2],cor_velha)] = [cor_velha]
            elif type(dic_cores[cor_nova]) == list and parametro1 == 1 and (parametro2 - aumento_esperado) == 0 and indice_da_cor(lista[-1],cor_nova) in dic_cores[cor_nova]:
                remover(cor_nova, indice_da_cor(lista[-1],cor_nova))



    
    #Antes das cores corretas serem encontradas
    if len(lista) != 0: 
        #Situacao em que ha mudanca da posicao e que a quantidade de cores certas e' a mesma das posicoes
        if  situacao[-1][1] != 0 and situacao[-1][1] == situacao[-1][0]:
           for i in range(4):
                dic_cores[lista[-1][i]] = (i)
                
        #Situacao em que todas as cores apresentadas estao na posicao errada
        elif situacao[-1][1] - aumento_esperado - posicao_esperada[-1] == 0:
            #Loop que vai remover todas as cores da listas de posicoes possiveis de uma determinada cor, caso a posicao original ainda não tenha sido encontrada
            for i in range(4):
                if type(dic_cores[lista[-1][i]]) == list and i in dic_cores[lista[-1][i]]:
                    remover(lista[-1][i], i)
                    #dic_cores[lista[-1][i]].remove(i)

        #Determinar o valor das posições corretas esperadas
        
    
    
    #Retirando as posicoes ja encontradas:
    copia_dic_cores = dic_cores.copy()
    
    for cor in copia_dic_cores:
        if type(copia_dic_cores[cor]) == int and cor in cores_certas:
            for k in copia_dic_cores:
                if type(copia_dic_cores[k]) == list and copia_dic_cores[cor] in copia_dic_cores[k]:
                    remover(k, dic_cores[cor])
                    #dic_cores[k].remove(copia_dic_cores[cor])
    
    #Analisar caso uma cor seja única em uma posição TESTE
    copia_dic_pos = dic_posicoes.copy()
    posicao_especial = 0
    cor_especial = 0
    for cor in cores_certas:
        contador = 0
        posicao_especial = []
        for posicao in copia_dic_pos:
            if cor in copia_dic_pos[posicao]:
                contador += 1
                posicao_especial = posicao
                cor_especial = cor
        if contador == 1 and len(dic_posicoes[posicao_especial]) > 1:
            dic_posicoes[posicao_especial] = [cor_especial]
    
    #Depois retirar as cores cujas posições já foram encontradas TESTE
    copia_dic_pos = dic_posicoes.copy()
    for posicao in copia_dic_pos:
        if len(dic_posicoes[posicao]) == 1:
            for k in copia_dic_pos:
                if len(copia_dic_pos[k]) > 1 and copia_dic_pos[posicao][0] in copia_dic_pos[k]:
                    dic_posicoes[k].remove(copia_dic_pos[posicao][0])

    
    
'''
A análise deve ver as posições possíveis e guardar depois verificar se a a cor correta 
Armazenar as posições das cores quando houver alguma posição correta em qualquer momento do código
parametro1 = diferença das cores
parametro2 = diferença das posições
lista = histórico de sequencia de cores
situacao = acerto das cores e posições
'''
def remover(cor,indice):
    '''Remove determinado índice na lista de posições possíveis de uma cor e a transforma para inteiro se for uma lista unitária'''
    global dic_cores
    global dic_posicoes #TESTE
    dic_cores[cor].remove(indice)
    if cor in dic_posicoes[indice]:
        dic_posicoes[indice].remove(cor) #TESTE
    if len(dic_cores[cor]) == 1:
        dic_cores[cor] = dic_cores[cor].pop()





def achar_substituir(lista, novo_item, velho_item):

    '''Recebe um lista e troca todos os elementos dela de valor <velho_item> pelo valor <novo_item>, e retorna essa lista'''

    for i in range(len(lista)):
        if lista[i] == velho_item:         
            lista[i] = novo_item
        
    return lista


def substituir_lista(lista1, lista2):
    '''Recebe 2 listas e coloca em lista 1 os itens de lista2 que não estão em lista 1 '''

    itens_diferentes = []
    l2 = lista2.copy()

    for i in range(len(lista1)):
        if lista1[i] not in l2:
            itens_diferentes.append(lista1[i])
        else:
            l2.remove(lista1[i])
            
    for item in itens_diferentes:
        lista1 = achar_substituir(lista1, l2[0], item)
        l2.pop(0)
    
    return lista1
    

        

