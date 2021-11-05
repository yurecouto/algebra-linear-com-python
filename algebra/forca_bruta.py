def geradora(numero, lenght):

    lista = list()
    tentativa = list()

    # Cria a lista primaria
    for n in range(-numero, (numero + 1)):
        lista.append(n)   

    
    for n1 in lista:
        for n2 in lista:

            if lenght > 2:
                for n3 in lista:

                    if lenght > 3:
                        for n4 in lista:

                            if lenght > 4:
                                for n5 in lista:
                                    tentativa.append([n1, n2, n3, n4, n5])

                            else:
                                tentativa.append([n1, n2, n3, n4])

                    else:
                        tentativa.append([n1, n2, n3])

            else:
                tentativa.append([n1, n2])

    return tentativa

'''print(teste(10, 3)[0])'''