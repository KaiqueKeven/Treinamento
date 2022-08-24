def palindromo(a):
    palavra = a.split()
    junto = ''.join(palavra)
    inverso = ''
    for letra in range(len(junto)-1, -1, -1):
        inverso += junto[letra]
    if inverso == junto:
        return 'e um palidromo'
    else:
        return 'não e um palidromo'


b = str(input('digite a sua palavra: '))
print(f'essa frase {b}: {palindromo(b)}')
