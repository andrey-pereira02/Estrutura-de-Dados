def KmenoresElementos(array: [], i):
    minHeap = minHeap()

    for numeros in array:
        minHeap.add(numeros)
    resultado = []

    for _ in range(i):
        resultado.append(minHeap.remover_min())
    return resultado
