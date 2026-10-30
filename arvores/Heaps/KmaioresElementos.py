def maioresK(array: [], i):
    maxHeap = maxHeap()

    for k in array:
        maxHeap.add(k)

    resultado = []

    for _ in range(i):
        resultado.append(maxHeap.remove_max())

    return resultado
