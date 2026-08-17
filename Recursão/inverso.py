def inverso(n, inv=0):

    if n == 0:
        return inv

    a = n % 10

    return inverso(n//10, a + 10*inv)


print(inverso(345))
