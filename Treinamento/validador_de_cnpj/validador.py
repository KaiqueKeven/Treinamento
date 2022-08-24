from blib_cnpj import filtra, validando1, validando2, formulal, gerando, formata

# gerando um CNPJ
g = formata(gerando())
print(g)

# filtrando os dados
cnpj = str(input('Digite seu CNPJ: '))
cnpj = filtra(cnpj)
novo_cnpj = filtra(cnpj)[:12]

# validando/verificando o penutimo digito
primeiro = validando1(novo_cnpj)
soma = formulal(primeiro)
novo_cnpj = novo_cnpj + soma

# validando/verificando o ultimo digito
segundo = validando2(novo_cnpj)
soma = formulal(segundo)
novo_cnpj = novo_cnpj + soma

# verificando ser o CNPJ e valido
if cnpj == novo_cnpj:
    print('Seu CNPJ e Valido')
else:
    print('Seu CNPJ e Invalido')