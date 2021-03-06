from math import sqrt 


# Soma de vetores
def soma_vetores(*vetores):

    lenght = len(vetores[0])
    vetor_soma = list()

    # Separa por index (sendo cada index uma dimensão do vetor)
    for index in range(0, lenght):

        # Faz a operação com a dimensão de cada vetor
        soma = list()
        for vetor in vetores:
            soma.append(vetor[index])

        vetor_soma.append(sum(soma))
        soma.clear
    
    return vetor_soma
            
'''print(soma_vetores([5, 3, -15], [-10, 20, 0], [3, -14, 6]))'''


# Soma de vetores em lista
def soma_vetores_lista(lista):

    lenght = len(lista[0])
    vetor_soma = list()

    for index in range(0, lenght):

        soma = list()
        for vetor in lista:
            soma.append(vetor[index])

        vetor_soma.append(sum(soma))
        soma.clear
    
    return vetor_soma
            
'''print(soma_vetores_lista([[5, 3, -15], [-10, 20, 0], [3, -14, 6]]))'''


# Subtração de vetores
def subtracao_vetores(vetor1, vetor2):

    # subtrai as respectivas dimensões
    a = list()
    for index in range(len(vetor1)):
        a.append(vetor1[index] - vetor2[index])

    return a

'''print(subtracao_vetores([10, 20], [-1, 3]))'''


# Multiplicação de vetores, Produto escalar
def produto_escalar(vetor1, vetor2):

    # multiplica vetor1 e vetor2
    a = list()
    for index in range(len(vetor1)):
        a.append(vetor1[index] * vetor2[index])

    # soma os resultados para obter o produto escalar
    ep = sum(a)

    return ep

'''print(produto_escalar([5, -1], [5, -1]))'''


# Multiplicação de vetores, Produto escalar
def multiplicar_vetor(vetor1, numero):

    # multiplica vetor1 e vetor2
    a = list()
    for index in range(len(vetor1)):
        a.append(vetor1[index] * numero)

    # soma os resultados para obter o produto escalar

    return a

'''print(multiplicar_vetor([2, 1], 3))'''


# Formula para calcular o módulo
def modulo_vetor(vetor):

    # faz a multiplicação do vetor por si mesmo
    m = produto_escalar(vetor, vetor)    

    # retorna a raiz quadrada do produlo escalar
    modulo = sqrt(m)
    
    return modulo

'''print(modulo_vetor([2,5,-7]))'''


# Formula para descobrir o cosseno de theta
def cos_theta(vetor1, vetor2):

    # multiplica vetor1 e vetor2
    m = produto_escalar(vetor1, vetor2)

    # primeiro modulo
    mod1 = modulo_vetor(vetor1)

    # segundo modulo
    mod2 = modulo_vetor(vetor2)

    #formula para obtenção do cosseno de theta
    cos = m / (mod1 * mod2)

    return cos

'''print(cos_theta([1,1,0], [2,1,-1]))'''


# Formula para ortogonalidade
def ortogonalidade_vetores(vetor1, vetor2):

    # Se vetor1 * vetor2 == 0, 
    # então o angulo theta entre eles será 90º 
    if produto_escalar(vetor1, vetor2) == 0:
        return True
    
    return False

'''print(ortogonalidade_vetores([4,4], [4,-4]))'''


# Formula da projeção ortogonal
def proj_ortogonal(vetor1, vetor2):

    # numerador
    numerador = produto_escalar(vetor1, vetor2)

    # denominador 
    denominador = produto_escalar(vetor2, vetor2)
   
    # Formula
    vetor_proj = list()
    for index in range(len(vetor1)):
        vetor_proj.append(f'{((numerador * vetor2[index]) / denominador):.2f}')

    return vetor_proj

'''print(proj_ortogonal([1,-3,2], [2,3,-5]))'''

