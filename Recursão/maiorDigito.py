def maiorDigito(n):

    if n < 10:
        return n

    a = n % 10
    m = maiorDigito(n//10)

    if m > a:
        return m
    else:
        return a


numero = maiorDigito(5879)
print(numero)
