def contaDigito(n):

    if n < 10:
        return 1

    return contaDigito(n//10) + 1


num = contaDigito(15555)
print(num)
