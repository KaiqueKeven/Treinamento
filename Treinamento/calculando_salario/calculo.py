'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu saláriono referido mês///, sabendo-se que são descontados 11% para o Imposto de Renda
, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

hora = int(input('Diga quanto ganha por Hora: '))
hora_trabalhada = float(input('Digite sua carga horaria de trabalho: '))
salario_bruto = (hora * hora_trabalhada) * 30
ir = salario_bruto * 11 / 100
inss = salario_bruto * 8 / 100
sindicato = salario_bruto * 5 / 100
salario_liquido = salario_bruto - ir - inss - sindicato

print()
print(f'Salario Bruto: R${salario_bruto:.2f}')
print(f'INSS (8%): R${inss:.2f} Discontado')
print(f'Sindicato (5%): R${sindicato:.2f} Discontado')
print(f'IR (11%): R${ir:.2f} Discontado')
print(f'Salario Liquido: R${salario_liquido:.2f}')
