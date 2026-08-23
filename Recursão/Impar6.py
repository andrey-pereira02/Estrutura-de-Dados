def impar6(n):
    if n < 10:
        if n % 2 == 0:
            return n
        else:
            return 6

    a = n % 10

    if a % 2 == 0:
        return impar6(n//10)*10 + a
    else:
        return impar6(n//10)*10 + 6


print(impar6(1234))
