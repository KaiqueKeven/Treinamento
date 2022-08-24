from random import randint


def filtra(cn):
    f = cn.replace('-', '').replace('.', '').replace('/', '')
    return f


def validando1(p):
    tot = 5
    acumolo = 0
    for n in p:
        n = int(n)
        soma = n * tot
        tot -= 1
        acumolo += soma
        if tot == 1:
            tot = 9
    return acumolo


def validando2(p):
    tot = 6
    acumolo = 0
    for n in p:
        n = int(n)
        soma = n * tot
        tot -= 1
        acumolo += soma
        if tot == 1:
            tot = 9
    return acumolo


def formulal(p):
    formula = 11 - (p % 11)
    if formula > 9:
        formula = 0
    formula = str(formula)
    return formula


def gerando():
    primeiro_b = randint(0, 9)
    segundo_b = randint(0, 9)
    terceiro_b = randint(100, 999)
    quarto_b = randint(100, 999)
    quinto_b = '0001'
    ibicio_npj = f'{primeiro_b}{segundo_b}{terceiro_b}{quarto_b}{quinto_b}'
    v = validando1(ibicio_npj)
    soma = formulal(v)
    novo = ibicio_npj + soma

    v = validando2(novo)
    soma = formulal(v)
    novo = novo + soma
    return novo


def formata(cnpj):
    cnpj = filtra(cnpj)
    formatando = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return formatando
