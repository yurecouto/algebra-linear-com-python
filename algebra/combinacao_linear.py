from math import perm
from vetores import multiplicar_vetor, produto_escalar, soma_vetores_lista
from forca_bruta import geradora


# Verifica se o vetor main é combinação dos outros vetores
def comb_linear(vetor_main, *vetores):   

    # Funciona com base em tentativa e erro 
    # a variavel teste é uma lista com vários conjuntos de possíveis escalares
    lenght = len(vetores)
    testes = geradora(20, lenght)

    # Verifica uma tentativa
    for teste in testes:

        lista = list()

        # Multiplica cada vetor por uma tentativa
        for index in range(0, len(teste)):
            lista.append(multiplicar_vetor(vetores[index], teste[index]))

        # Soma dos vetores em lista
        vetor_soma = soma_vetores_lista(lista)

        # Se a soma dos vetores for igual ao vetor principal, 
        # retorna positivo a combinação linear
        if vetor_main == vetor_soma:
            return True
    
    return False

'''print(comb_linear([1, 2, 4], [1, 2, 1], [1, 5, 2], [1, 1, 0]))'''


# Verifica se os vetores são linearmente independentes ou dependentes
def dependencia_linear(*vetores):   

    # Funciona com base em tentativa e erro 
    # a variavel teste é uma lista com vários conjuntos de possíveis escalares
    lenght = len(vetores)
    testes = geradora(10, lenght)
    zero_soma = list()
    zero_escalares = list()

    # vetor zero para ser igualado
    for z in vetores[0]:
        zero_soma.append(0)

    # escalares zero
    for z in vetores:
        zero_escalares.append(0)

    # Verifica uma tentativa
    for teste in testes:

        lista = list()

        # Multiplica cada vetor por uma tentativa
        for index in range(0, len(teste)):
            lista.append(multiplicar_vetor(vetores[index], teste[index]))

        soma = soma_vetores_lista(lista)

        print(f'{teste} ===> {soma}\n')
        
    
        if soma == zero_soma:
            if teste == zero_escalares:
                return 'LI'
            
            else:
                return 'LD'

print(dependencia_linear([1, 0], [1, 1]))

