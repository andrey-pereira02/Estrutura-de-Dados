def soma2(n: list, target, i, j):

    if i >= j:
        return False

    soma = n[i] + n[j]

    if soma == target:
        return True

    if soma <= target:
        return soma2(n, target, i+1, j)

    else:
        return soma2(n, target, i, j-1)


S = [1, 3, 4, 6, 8, 10]
target = 14

resultado = soma2(S, target, 0, len(S) - 1)

print(resultado)
