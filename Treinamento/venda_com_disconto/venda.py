'''Um comerciante quer vender seus produtos com um lucro de 45% caso o valor da compra for menor que R$30,00.
 Caso contrário, o lucro deverá ser de 30%.
 Faça um programa que recebe o valor do produto e devolve o valor da venda.'''

produto = float(input('Digite o valor do produto: '))

if produto < 30:
    valor = produto + (produto * 45 / 100)
else:
    valor = produto + (produto * 30 / 100)

print(f'O valor de venda e {valor}')
