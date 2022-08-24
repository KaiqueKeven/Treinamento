from random import choices
from string import ascii_letters, digits

letras = ascii_letters
digitos = digits
caracteris = '!@#$%&+?*'
geral = letras + digitos + caracteris
senha = ''.join(choices(geral, k=10))
print(senha)

