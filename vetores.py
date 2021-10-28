from math import sqrt 

# Soma de vetores
def soma_vetores(vetor1, vetor2):

    # soma as respectivas dimensões
    a = list()
    for index in range(len(vetor1)):
        a.append(vetor1[index] + vetor2[index])

    return a

'''print(soma_vetores([-1, 3], [10, 20]))'''


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

'''print(produto_escalar([1, 2], [5, 3]))'''


# Formula para calcular o módulo
def modulo(vetor):

    # faz a multiplicação do vetor por si mesmo
    m = produto_escalar(vetor, vetor)    

    # retorna a raiz quadrada do produlo escalar
    modulo = sqrt(m)
    
    return modulo

'''print(modulo([2,5,-7]))'''


# Formula para descobrir o cosseno de theta
def cos_theta(vetor1, vetor2):

    # multiplica vetor1 e vetor2
    m = produto_escalar(vetor1, vetor2)

    # primeiro modulo
    mod1 = modulo(vetor1)

    # segundo modulo
    mod2 = modulo(vetor2)

    #formula para obtenção do cosseno de theta
    cos = m / (mod1 * mod2)

    return cos

'''print(cos_theta([1,1,0], [2,1,-1]))'''


# Formula para ortogonalidade
def ortogonalidade(vetor1, vetor2):

    # Se vetor1 * vetor2 == 0, 
    # então o angulo theta entre eles será 90º 
    if produto_escalar(vetor1, vetor2) == 0:
        return True
    
    return False

'''print(ortogonalidade([4,4], [4,-4]))'''


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