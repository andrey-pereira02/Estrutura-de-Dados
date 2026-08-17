def removePares(n):

    if n < 10:
        if n % 2 == 0:
            return 0
        else:
            return n

    a = n % 10

    if a % 2 == 0:
        return removePares(n//10)

    return removePares(n//10) * 10 + a


print(removePares(345))
