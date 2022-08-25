"""Você tem 9 pesos e sabe que 1 deles é mais pesado que os demais,você precisa descobrir qual é.
  Para isso você alugou uma balança de pratos e tem direito de utilizá-la 3 vezes.
 Desenvolva um algoritmo que execute a sequência de passos que deve ser realizada."""

from random import randint

maior = 0
tentativa = 3
for i, p in enumerate(range(1, 10)):
    peso = randint(1, 100)
    if i == 0:
        maior = peso
    else:
        if peso > maior:
            maior = peso

while True:
    jogador = int(input('Qual e o peso mais pesado? '))
    tentativa -= 1
    if jogador == maior:
        print('Parabéns você Venceu!')
        break
    else:
        print(f'Errado, você tem mais {tentativa} tentativa')
    if tentativa == 0:
        print(f'maior {maior}')
        print('Oooo!, mais sorte na proxima')
        break


    
    