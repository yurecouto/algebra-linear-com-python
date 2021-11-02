from vetores import multiplicar_vetor, produto_escalar
from random import randint, choice, sample


def geradora(numero, lenght):

    lista = list()

    # Cria a lista primaria
    for n in range(-numero, (numero + 1)):
        lista.append(n)   
     


print(geradora(5, 2))

'''
def comb_linear(vetor_main, *vetores):   

    lenght = len(vetores)
    errors = list()
    produto_principal = produto_escalar(vetor_main, vetor_main)

       
print(comb_linear([1, 2, 4], [1, 2, 1], [1, 0, 2], [1, 1, 0]))
'''
