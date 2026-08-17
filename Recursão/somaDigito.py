def somaDigito(n):

    if n < 10:
        return n

    a = n % 10
    return a + somaDigito(n//10)


print(somaDigito(15))
