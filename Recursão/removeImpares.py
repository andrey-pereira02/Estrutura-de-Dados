def removeImpares(n):

    if n < 10:
        if n % 2 == 0:
            return n
        else:
            return 0

    a = n % 10

    if a % 2 != 0:
        return removeImpares(n//10)

    return removeImpares(n//10) * 10 + a


print(removeImpares(254))
