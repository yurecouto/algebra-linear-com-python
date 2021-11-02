from vetores import multiplicar_vetor, produto_escalar


a = [[] * 4]
print(a)


'''
    lenght = len(vetores)
    errors = list()
    produto_principal = produto_escalar(vetor_main, vetor_main)

    # Primeiro criamos valores que serão testados via tentativa e erro
    while True:
        teste = sample(range(-10, 10), lenght)

        if teste not in errors:
            vetores_teste = list()
            produtos_escalares = list()
            
            # Aqui multiplicamos os vetores pelos valores gerados anterioirmente
            for index in range(0, lenght):
                vetor_teste = multiplicar_vetor(vetores[index], teste[index])
                vetores_teste.append(vetor_teste)

            # Fazemos o produto escalar de cada vetor 
            for vetor_teste in vetores_teste:
                pe = produto_escalar(vetor_teste, vetor_teste)
                produtos_escalares.append(pe)
                    
            # Soma dos produtos escalares        
            soma = sum(produtos_escalares)

            if soma == produto_principal:
                return True

            # Adicionamos o conjunto de tentativa aos erros (se estiver na lista de erros, não será calculado)
            errors.append(teste)

            vetores_teste.clear()
            produtos_escalares.clear()

        else:    
            print(teste)
'''