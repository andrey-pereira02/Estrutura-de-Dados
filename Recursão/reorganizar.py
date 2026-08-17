def reorganizar(n: list, target, position=0):

    if target in n:
        return n

    for i in range(len(n)):
        if n[i] == target:
            position = i

    for k in range(len(n)):
        if n[k] > target:
            flag = n[k]
            n[position+1] = n[k]
            n[k] = flag
            return reorganizar(n, target, position)
        elif n[k] < target:
            flag = n[k]
            n[position-1] = n[k]
            n[k] = flag
            return reorganizar(n, target, position)
