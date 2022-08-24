def formataip(parametro):
    p = parametro.replace('.', '').replace('/', '')
    return p


def binario(valor):
    valor = [valor[:2], valor[2:4], valor[4:6], valor[6:8]]
    lista = []
    bi = [128, 64, 32, 16, 8, 4, 2, 1]
    tot = cont = 0
    while True:
        for i, bina in enumerate(bi):
            if int(valor[cont]) >= bina:
                tot += bina
                if int(valor[cont]) >= tot:
                    lista.append(1)
                else:
                    tot -= bina
                    lista.append(0)
            else:
                lista.append(0)
        tot = 0
        cont += 1
        if cont == 4:
            break
    return lista


def bits(valor, a):
    totb = 0
    bit = []
    while True:
        for ip in valor:
            if a == 0:
                bit.append(0)
            else:
                bit.append(1)
                a -= 1
                totb += 1
        if len(bit) == 32:
            break
    return bit


def broadcast(valor):
    bro = []
    tot = cont = 0
    bi = [128, 64, 32, 16, 8, 4, 2, 1]
    for ip in valor:
        cont += 1
        if ip == 1:
            for bina in bi:
                if bina == bi[cont-1]:
                    tot += bina
                if tot == 255:
                    bro.append(tot)
                    tot = cont = 0
    if tot != 0:
        bro.append(tot)
    return bro


def rede(valor, novo_ip):
    red = []
    novo = []
    b = 32
    tot = 0
    for x in valor:
        if x == 1:
            tot += 1
    for y in range(8, 33, 8):
        if tot > y:
            for x in range(0, 8):
                red.append(1)
        else:
            for x in range(0, 8):
                red.append(0)
    for i, p in enumerate(novo_ip):
        r = red[i]
        if r == 1:
            novo.append(p)
        else:
            novo.append(0)
    return novo


def nova_rede(novo_ip, novo, temp):
    cont = certo = im = 0
    novo_p = []
    for i, p in enumerate(novo_ip):
        if cont <= 8:
            cont += 1
            if p == novo[i]:
                certo += 1
                if certo == 8:
                    novo_p.append(int(temp[im]))
                    im += 1
                    certo = 0
            else:
                novo_p.append(0)
                break
        else:
            cont = 0
    novo_p.append(int(temp[4]))
    return novo_p


def mascara(novo_ip, novo, temp):
    cont = certo = im = 0
    novo_p = []
    for i, p in enumerate(novo_ip):
        if cont <= 8:
            cont += 1
            if p == novo[i]:
                certo += 1
                if certo == 8:
                    novo_p.append(int(temp[im]))
                    im += 1
                    certo = 0
            else:
                novo_p.append(1)
                break
        else:
            cont = 0
    novo_p.append(int(temp[4]))

    return novo_p


def primeiro_ip(novo_ip, novo, temp, ip_validoso):
    cont = certo = im = 0
    novo_p = []
    for i, p in enumerate(novo_ip):
        if cont <= 8:
            cont += 1
            if p == novo[i]:
                certo += 1
                if certo == 8:
                    novo_p.append(int(temp[im]))
                    im += 1
                    certo = 0
            else:
                novo_p.append(ip_validoso)
                break
        else:
            cont = 0
    novo_p.append(int(temp[4]))

    return novo_p
