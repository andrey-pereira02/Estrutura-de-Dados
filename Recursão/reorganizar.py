def reorganiza(S, k):
    if len(S) == 1:
        return S

    a = S[0]
    b = S[1:]

    if a < k:
        return [a] + reorganiza(b, k)
    else:
        return reorganiza(b, k) + [a]


n = [9, 4, 6, 7, 8, 2, 3]
k = 5
print(reorganiza(n, k))

"""Usando pop,insert e append"""


def muda(n, k):
    if len(n) == 1:
        return n

    a = n.pop()

    if a < k:
        n.insert(0, a)
    else:
        n.append(a)

    return muda(n, k)
