
def teste(n):
    lista = list()
    for c in range(0, n):
        for t in range(-10, 11):
            lista.append(t)

    for n in range(0, len(lista), 10):
        return n

print(teste(5))
