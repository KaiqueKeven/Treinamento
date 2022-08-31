'''Escreva uma função que recebe um vetor de números e escreva no console quais números aparecem mais de uma vez e a quantidade de repetições. Exemplo:
(1, 1, 2, 3, 4, 3, 1)
Número 1: 3 vezes
Número 3: 2 vezes '''


def contagem(*args):
    listas = [x for x in args]
    cont = tot = 0
    for numero in args:
        cont = tot = 0
        for lista in listas:
            if numero == lista:
                cont += 1
            if cont > 1:
                if cont > tot:
                    tot = cont
        if tot > 1:
            print(f'numero {numero}: {tot} vezes')
            listas = [x for x in listas if not numero == x]


contagem(1, 2, 2, 3, 4, 4, 5, 6, 2, 2, 2, 4, 1)
