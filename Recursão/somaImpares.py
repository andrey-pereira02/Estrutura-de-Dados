def somaImpares(n):
    if n < 10:
        if n % 2 == 0:
            return 0
        else:
            return n

    a = n % 10
    if a % 2 == 0:
        return somaImpares(n//10)
    else:
        return somaImpares(n//10) + a


print(somaImpares(2235))
