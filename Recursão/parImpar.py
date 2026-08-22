def parImpar(n, pares=0, impares=0):
    if n == 0:
        return pares * 10 ** len(str(impares)) + impares

    a = n % 10

    if a % 2 == 0:
        return parImpar(n//10, pares*10 + a, impares)
    else:
        return parImpar(n//10, pares, impares*10 + a)


print(parImpar(1234))
