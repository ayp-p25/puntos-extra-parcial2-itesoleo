def contar_divisores(numero):
    numero_str = str(numero)
    contador = 0
    for digito in numero_str:
        if digito != '0' and numero % int(digito) == 0:
            contador += 1
    return contador
