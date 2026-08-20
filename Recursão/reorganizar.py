def reorganiza(S, inicio, fim, k):
    if inicio >= fim:
        return

    if S[inicio] <= k:
        reorganiza(S, inicio + 1, fim, k)

    elif S[fim] > k:
        reorganiza(S, inicio, fim - 1, k)

    else:
        S[inicio], S[fim] = S[fim], S[inicio]
        reorganiza(S, inicio + 1, fim - 1, k)


S = [8, 3, 7, 2, 9, 1, 5]
k = 5

reorganiza(S, 0, len(S) - 1, k)

print(S)
