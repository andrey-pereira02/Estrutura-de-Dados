def contaParImpar(n, pares=0, impares=0):
    if n < 10:
        if n % 2 == 0:
            pares += 1
        elif n % 2 != 0:
            impares += 1
        return "impares = " + str(impares) + " pares = " + str(pares)

    a = n % 10

    if a % 2 == 0:
        pares += 1
    else:
        impares += 1

    return contaParImpar(n//10, pares, impares)


print(contaParImpar(1234))
