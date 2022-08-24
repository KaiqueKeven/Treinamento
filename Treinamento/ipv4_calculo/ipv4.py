from funcao import *


ip = '.20.12.45/26'
novo_ip = formataip(ip)

temp = [novo_ip[:2], novo_ip[2:4], novo_ip[4:6], novo_ip[6:8], novo_ip[8:]]
a = int(novo_ip[8:])
binario = binario(novo_ip)

ip_validos = 2 ** (len(binario) - a) - 2
bits = bits(binario, a)

broadcast = broadcast(bits)

r = rede(bits, binario)
rede = nova_rede(binario, r, temp)

mascara = mascara(binario, r, temp)

primeiro_ip = primeiro_ip(binario, r, temp, ip_validos)
print(f'IP : {novo_ip}')
print(f'Rede: {rede}')
print(f'Broadcast: {broadcast}')
print(f'Mascara: {mascara}')
print(f'Primeiro IP: {primeiro_ip}')
print(f'Nº de IPS: {ip_validos}')
